import socket

def connect_to_init_server(server_ip, server_port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            # Connect to the server
            client_socket.connect((server_ip, server_port))
            print(f"Connected to server at {server_ip}:{server_port}")
 
            # Interaction loop
            while True:
                # Receive and print the server prompt or message
                server_message = client_socket.recv(1024).decode()
                if not server_message:
                    break  # Exit loop if no message is received
                print(server_message, end='')

                # Check for specific exit command or condition if needed
                if "exit message or condition" in server_message:
                    print("Exiting as per server's request.")
                    break

                # Read user input and send it to the server
                client_input = input()
                client_socket.send(client_input.encode() + b'\n')

            

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            print("Connection closed.")

# Replace with the actual server IP and port
SERVER_IP = '10.0.2.15'  # Example IP
SERVER_PORT = 20100  # Port number as per the server code

connect_to_init_server(SERVER_IP, SERVER_PORT)
