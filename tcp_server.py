import socket
import threading

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 5050         # Port to listen on

def process_message(msg):
    """
    Processes the incoming string based on the lab rules.
    """
    if not msg:
        return msg
        
    first_char = msg[0]
    
    if first_char == 'A':
        # Sort characters in descending order
        return ''.join(sorted(msg, reverse=True))
    elif first_char == 'C':
        # Sort characters in ascending order
        return ''.join(sorted(msg))
    elif first_char == 'D':
        # Convert the entire string to uppercase
        return msg.upper()
    else:
        # If any other character, return the exact same message
        return msg

def handle_client(conn, addr):
    """
    Handles communication with a single connected client.
    """
    print(f"[NEW CONNECTION] TCP Client {addr} connected.")
    connected = True
    
    while connected:
        try:
            # Receive data from the client (blocking call)
            msg = conn.recv(1024).decode('utf-8').strip()
            
            if not msg:
                break # Client disconnected
                
            print(f"[{addr}] Received: {msg}")
            
            # Process the message according to rules
            processed_msg = process_message(msg)
            
            # Send the response back to the client
            conn.send((processed_msg + '\n').encode('utf-8'))
            
        except ConnectionResetError:
            break # Handle abrupt client disconnections safely

    print(f"[DISCONNECT] TCP Client {addr} disconnected.")
    conn.close()

def start_tcp_server():
    """
    Starts the TCP server and listens for incoming connections.
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] TCP Server is listening on {HOST}:{PORT}")
    
    try:
        while True:
            # Accept new connections
            conn, addr = server.accept()
            
            # Start a new thread for the client
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            
            # Active count minus 1 to exclude the main server thread
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
    except KeyboardInterrupt:
        print("\n[SHUTDOWN] Server is shutting down.")
        server.close()

if __name__ == "__main__":
    start_tcp_server()
