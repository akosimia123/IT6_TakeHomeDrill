import socket
import time

HOST = '127.0.0.1'  # localhost address (the server is running on the same machine)
PORT = 8888 # port number where the server is listening

def send_pin(pin):
    # Create the body of the POST request
    body = f'magicNumber={pin}' 
    
    # Create the POST request manually
    request = ( 
        f"POST /verify HTTP/1.1\r\n" 
        f"Host: {HOST}:{PORT}\r\n"
        f"Content-Type: application/x-www-form-urlencoded\r\n" 
        f"Content-Length: {len(body)}\r\n" 
        f"Connection: close\r\n" 
        f"\r\n"
        f"{body}" 
    )
    
    # Create a new socket for each request
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
        s.connect((HOST, PORT)) 
        s.sendall(request.encode()) 
        response = s.recv(4096) 
        return response.decode() 