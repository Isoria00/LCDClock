from flask import Flask                                                                 # Import Flask Web Framework
from datetime import datetime                                                           # Imports datetime for to work with dates and times
import serial                                                                           # How to tell Python to use the pyserial library to communicate with serial devices
import time                                                                             # Lets us work with the time module
import threading                                                                        # Lets us run multiple tasks at the same time

app = Flask(__name__)                                                                   # Creates Flask app instance

# You can Replace 'COM5' with whatever your Serial Port is
ser = serial.Serial('COM5', 9600, timeout=1)                                            # 9600 is baud rate , timeout means wait 1 sec for data
time.sleep(2)                                                                           # Wait for Arduino to reset after serial connection

def send_date_time_forever():                                                           # Function to continuously send date and time to arduino over serial
    while True:
        now = datetime.now()                                            
        date_str = now.strftime("%A %d, %Y")                                            # Format date: Friday 30, 2025 
        time_str = now.strftime("%I:%M%p").lstrip('0')                                  # Format time: 12-hour clock with AM/PM, no seconds
        send_str = f"{date_str}|{time_str}\n"                                           # Create message with a | seperator and newline
        ser.write(send_str.encode())                                                    # Send the message to the Arduino as bytes
        time.sleep(1)                                                                   # Wait 1 second before sending again

threading.Thread(target=send_date_time_forever, daemon=True).start()                    # Start the background thread that sends time to Arduino

@app.route('/')                                                                         # Define the main Flask route for the web page
def index():                    
    return "<h1>Sending formatted date and time to Arduino...</h1>"                     # ***You can build on top of this add whatever you want***

if __name__ == '__main__':                                                              # Run the Flask App
    app.run(host='0.0.0.0', port=5000)
