""" Where our GUI - Frontend code will live, as well as be responsible
for sending messages to the Arduino"""

import FreeSimpleGUI as sg

sg.theme("LightBlue")

""" Widgets start! """
choose_label = sg.Text("Choose your button", key="choose_label")
lock_btn = sg.Button("Lock", key="lock_btn", pad=(50, 50), button_color="Red")
unlock_btn = sg.Button("Unlock", key="unlock_btn", pad=(50, 50), button_color="Green")
exit_btn = sg.Button("Exit")
status_label = sg.Text("The locker is currently", key="status_label", pad=(40,20))
status = sg.Text(key="status")

""" Widgets end! """

layout = [[choose_label],
          [lock_btn, unlock_btn],
          [status_label, status]]

window = sg.Window("Lock-The-Mechanism-Controller",layout=layout, font=('Helvetica', 20)) #, size=(500,500)

while True:
    event, values = window.read() # type: ignore
    
    if event == sg.WIN_CLOSED or window.was_closed():
        break
    
    match event:
        case "lock_btn":
            window["status"].update(value="LOCKED") # type: ignore

        case "unlock_btn":
            window["status"].update(value="UNLOCKED!") # type: ignore

        case "Exit":
            break
        
        case sg.WIN_CLOSED:
            break

print("bye bye!")
window.close()