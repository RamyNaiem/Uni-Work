// Function to generate an RSA key pair
async function generateKeyPair() {
    const keyPair = await window.crypto.subtle.generateKey(
        {
            name: "RSA-OAEP",
            modulusLength: 2048, 
            publicExponent: new Uint8Array([1, 0, 1]),
            hash: "SHA-256",
        },
        true,
        ["encrypt", "decrypt"]
    );
    return keyPair;
}

// Function to export the public key in a format that can be sent over the network
async function exportPublicKey(keyPair) {
    const exported = await window.crypto.subtle.exportKey(
        "spki",
        keyPair.publicKey
    );
    return new Uint8Array(exported);
}

// Function to encrypt a message with the recipient's public key
async function encryptMessage(publicKey, message) {
    const encodedMessage = new TextEncoder().encode(message);
    const encrypted = await window.crypto.subtle.encrypt(
        {
            name: "RSA-OAEP"
        },
        publicKey,
        encodedMessage
    );
    return new Uint8Array(encrypted);
}

// Function to decrypt a message with the user's private key
async function decryptMessage(privateKey, encrypted) {
    const decrypted = await window.crypto.subtle.decrypt(
        {
            name: "RSA-OAEP"
        },
        privateKey,
        encrypted
    );
    return new TextDecoder().decode(decrypted);
}

// Example Usage
async function exampleUsage() {
    try {
        const keyPair = await generateKeyPair();
        const exportedPublicKey = await exportPublicKey(keyPair);
        
        // Example: Convert exported public key to Base64 to send it to the server
        const base64PublicKey = btoa(String.fromCharCode.apply(null, exportedPublicKey));

        console.log("Base64 Public Key:", base64PublicKey);
        
        // Encrypt a message using the public key
        const encryptedMessage = await encryptMessage(keyPair.publicKey, "Hello, secure world!");

        // Decrypt the message using the private key
        const decryptedMessage = await decryptMessage(keyPair.privateKey, encryptedMessage);

        console.log("Decrypted Message:", decryptedMessage);
    } catch (error) {
        console.error("Encryption error:", error);
    }
}

// Uncomment the following line to test the example usage
// exampleUsage();
