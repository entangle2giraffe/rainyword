import PySimpleGUI as sg
import app
import sender.player as player

# Define the window's contents
# layout = [[sg.Text("What's your name?")],
#           [sg.Input(key='-INPUT-')],
#           [sg.Text(size=(40,1), key='-OUTPUT-')],
#           [sg.Button('Ok'), sg.Button('Quit'), sg.Button('Reset')]]

layout = [[sg.Text(size=(40,1), key='-NUMCLIENT-')],
          [sg.Text(size=(40,1), key='-RESET-')],
          [sg.Button('Start'), sg.Button('Reset'), sg.Button('Quit')]]

# Create the window
window = sg.Window('RainyWords Server', layout)



# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()

    numClients = len(app.Server.connections)
    n = len(player.player_list)
    window['-NUMCLIENT-'].update(str(numClients) + ' clients are connected')

    msg = '{"resetGame":1}'

    if event == 'Reset':
        # send reset json
        window['-RESET-'].update('Reset button clicked')
        print("Reset all games and scores")
        app.Server.announce(app.Server, msg)


    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

window.close()