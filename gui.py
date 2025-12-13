""" Where our GUI - Frontend code will live, as well as be responsible
for sending messages to the Arduino"""

import FreeSimpleGUI as sg
import serial
import time

sg.theme("LightBlue")

# Setup serial connection to Arduino
# Change 'COM3' to your Arduino's port
try:
    arduino = serial.Serial('COM4', 9600, timeout=1)
    time.sleep(2)  # Wait for Arduino to initialize
    print("Connected to Arduino")
except Exception as e:
    print(f"Failed to connect to Arduino: {e}")
    arduino = None

""" Widgets start! """
choose_label = sg.Text("Choose your button", key="choose_label", pad=(60,1))
lock_btn = sg.Button("Lock", key="lock_btn", pad=(50, 25), button_color="Red")
unlock_btn = sg.Button("Unlock", key="unlock_btn", pad=(50, 25), button_color="Green")
exit_btn = sg.Button("Exit", key="exit_btn")
status_label = sg.Text("The locker is currently:", key="status_label", pad=(50,1))
status = sg.Text("______", key="status")
""" Widgets end! """

layout = [[choose_label],
          [lock_btn, unlock_btn],
          [status_label, status]]

window = sg.Window("Lock-The-Mechanism",
                   layout=layout,
                   font=('Helvetica', 20)) 

while True:
    event, values = window.read() # type: ignore
    
    if event == sg.WIN_CLOSED or window.was_closed():
        break
    
    match event:
        case "lock_btn":
            print("locked")
            if arduino:
                arduino.write(b"locked\n")  # Send "locked" to Arduino
                window["status"].update(value="LOCKED❌") # type: ignore

        case "unlock_btn":
            print("unlocked")
            if arduino:
                arduino.write(b"unlocked\n")
                window["status"].update(value="UNLOCKED✅") # type: ignore

        case "Exit":
            break
        
        case sg.WIN_CLOSED:
            break

if arduino:
    arduino.close()  # Close serial connection
print("bye bye!")
window.close()