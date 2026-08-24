import socket

# Server configuration
HOST = '127.0.0.1'
PORT = 5051

def process_message(msg):
    """
    Processes the incoming string based on the lab rules.
    """
    if not msg:
        return msg
        
    first_char = msg[0]
    
    if first_char == 'A':
        return ''.join(sorted(msg, reverse=True))
    elif first_char == 'C':
        return ''.join(sorted(msg))
    elif first_char == 'D':
        return msg.upper()
    else:
        return msg

def start_udp_server():
    """
    Starts the UDP server to receive datagrams.
    """
    # Use SOCK_DGRAM for UDP
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((HOST, PORT))
    print(f"[LISTENING] UDP Server is listening on {HOST}:{PORT}")
    
    try:
        while True:
            # Receive data and the address of the sender
            data, addr = server.recvfrom(1024)
            msg = data.decode('utf-8').strip()
            
            if msg:
                print(f"[{addr}] Received: {msg}")
                processed_msg = process_message(msg)
                
                # Send the processed message back to the sender's address
                server.sendto((processed_msg + '\n').encode('utf-8'), addr)
                
    except KeyboardInterrupt:
        print("\n[SHUTDOWN] UDP Server is shutting down.")
        server.close()

if __name__ == "__main__":
    start_udp_server()
