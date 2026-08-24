import socket

def tcp_client():
    HOST = '127.0.0.1'
    PORT = 5050
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((HOST, PORT))
        print("--- Connected to TCP Server ---")
        print("Type a string starting with A, C, or D (or type 'quit' to exit).")
        
        while True:
            msg = input("> ")
            if msg.lower() == 'quit':
                break
                
            # Send message to the TCP server
            client.send(msg.encode('utf-8'))
            
            # Receive response
            response = client.recv(1024).decode('utf-8').strip()
            print(f"Server Response: {response}")
            
    except ConnectionRefusedError:
        print("Error: TCP Server is not running.")
    finally:
        client.close()

def udp_client():
    HOST = '127.0.0.1'
    PORT = 5051
    
    # Use SOCK_DGRAM for UDP
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print("--- Ready to send to UDP Server ---")
    print("Type a string starting with A, C, or D (or type 'quit' to exit).")
    
    while True:
        msg = input("> ")
        if msg.lower() == 'quit':
            break
            
        # Send message to the UDP server address
        client.sendto(msg.encode('utf-8'), (HOST, PORT))
        
        # Receive response from the server
        response, server_addr = client.recvfrom(1024)
        print(f"Server Response: {response.decode('utf-8').strip()}")
        
    client.close()

if __name__ == "__main__":
    print("Which protocol would you like to test?")
    choice = input("Enter TCP or UDP: ").strip().upper()
    
    if choice == 'TCP':
        tcp_client()
    elif choice == 'UDP':
        udp_client()
    else:
        print("Invalid choice. Please run the script again and type TCP or UDP.")
