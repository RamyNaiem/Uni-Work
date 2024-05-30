from flask import Flask, request, render_template, redirect, url_for, session, flash
import sqlite3
import bcrypt
from werkzeug.utils import secure_filename
from cryptography.fernet import Fernet
import os
import io
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# Generate a key for AES
aes_key = os.urandom(32)  # AES key should be either 16, 24, or 32 bytes long

def encrypt_aes(data):
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()

    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(os.urandom(16)), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(padded_data) + encryptor.finalize()

    return ct

def decrypt_aes(encrypted_data):
    cipher = Cipher(algorithms.AES(aes_key), modes.CBC(os.urandom(16)), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(decrypted_data) + unpadder.finalize()

    return data.decode()





# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your secret key
DATABASE = 'database.db'
UPLOAD_FOLDER = 'uploads'

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Generate RSA Key Pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)
public_key = private_key.public_key()

# Function to encrypt data
def encrypt_data(public_key, data):
    encrypted = public_key.encrypt(
        data.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted

# Function to decrypt data
def decrypt_data(private_key, encrypted_data):
    decrypted = private_key.decrypt(
        encrypted_data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return decrypted.decode()

def sign_message(private_key, message):
    message = message.encode()
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

def verify_signature(public_key, message, signature):
    message = message.encode()
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except (ValueError, TypeError):
        return False


@app.route('/save_data', methods=['POST'])
def save_data():
    data = request.form['sensitive_data']
    encrypted_data = encrypt_data(public_key, data)

    # Code to save encrypted_data to the database
    # ...

    return 'Data saved successfully'

@app.route('/get_data')
def get_data():
    # Code to retrieve encrypted_data from the database
    # ...

    decrypted_data = decrypt_data(private_key, encrypted_data)
    return f'Decrypted Data: {decrypted_data}'


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with app.app_context():
        db = get_db_connection()
        db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL
            );
        ''')
        db.execute('''
            CREATE TABLE IF NOT EXISTS uploaded_files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                username TEXT NOT NULL,
                upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')
        db.commit()
        db.close()

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode('utf-8')
        password_hash = bcrypt.hashpw(password, bcrypt.gensalt())

        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)',
                         (username, password_hash))
            conn.commit()
        except sqlite3.IntegrityError:
            flash('Username already exists')
            return render_template('register.html')
        finally:
            conn.close()

        return redirect(url_for('login'))

    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode('utf-8')

        conn = get_db_connection()
        user = conn.execute('SELECT password_hash FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()

        if user and bcrypt.checkpw(password, user['password_hash']):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials')
            return render_template('login.html')

    return render_template('login.html')

# Logout route
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Home route
@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return render_template('index.html')

# File upload route
@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file:
            filename = secure_filename(file.filename)
            file_content = file.read()
            encrypted_content = cipher_suite.encrypt(file_content)

            conn = get_db_connection()
            conn.execute('INSERT INTO uploaded_files (filename, username) VALUES (?, ?)',
                         (filename, session['username']))
            conn.commit()
            conn.close()

            with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'wb') as encrypted_file:
                encrypted_file.write(encrypted_content)

            flash('File successfully uploaded and encrypted')
            return redirect(url_for('user_files'))

    return render_template('upload_file.html')

@app.route('/user_files')
def user_files():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    conn = get_db_connection()
    rows = conn.execute('SELECT filename FROM uploaded_files WHERE username = ?', (username,)).fetchall()
    conn.close()

    files = [row['filename'] for row in rows]  # Extract filenames from rows
    return render_template('file_list.html', files=files)


@app.route('/download_file/<filename>', methods=['GET'])
def download_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    if os.path.exists(file_path):
        with open(file_path, 'rb') as file:
            encrypted_content = file.read()

        decrypted_content = cipher_suite.decrypt(encrypted_content)
        return io.BytesIO(decrypted_content), 200, {
            'Content-Type': 'application/octet-stream', 
            'Content-Disposition': f'attachment; filename={filename}'
        }
    else:
        flash('File not found')
        return redirect(url_for('user_files'))


if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)

