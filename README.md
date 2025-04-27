
## IT6 Take Home Drill - 3-Digit PIN Brute Force

## Description
    This project is a Python brute-force script to find a 3-digit PIN on a local web server.  
    It uses only the `socket` library to manually create and send HTTP POST requests.  
    The project follows the IT6 drill rules, handles server slowdowns, and detects when the correct PIN is found.

## Getting Started
    - I downloaded executable file
    - Run ctf1_for_x64.exe file
    - Open CMD, Using <netstat -ano | findstr LISTENING> commands to find which port does excutable file listens.
    - Open Browser and put the address http://127.0.0.1:8888/ to see the Server Web Application.

## Crafting a Post request
    - I manually attempt to enter a password(pin) in web app to obeserve  its behaviour.
    - Open wireshark and filter HTTP to see the requests made and do follow http stream.
    - I manually created an HTTP POST request in my script following the correct format, including:
        #Request line: `POST /verify HTTP/1.1`
        #Host header
        #Content-Type
        #Content-Length
        #Connection close
        #Body containing the `magicNumber=PIN`

## Brutforce Strategy
    - I created PythonScript containing a loop that tries all PIN's from '000' to '999'.
    - Open and Run PythonScript.py
    - After each try, the script checks if the response contains `"ACCESS GRANTED"`. If yes, it prints the successful PIN and stops.

## 5. Handling Server Constraints
    - The server delays responses after too many wrong attempts.
    -To avoid message "whoa, slow down!" I added a `time.sleep(1)` to delay after each attempt.

## Access Granted Information
    - If the Script finally responce "ACCESS GRANTED". 
    - It display Correct PIN.
    - I go back to browser and put that correct pin and yes, I access the Web App.

    
    
    
    

        

