import FreeSimpleGUI as sg
from openai import OpenAI 
#imports
#API Key
client = OpenAI(api_key="**")

#Layout of the window
layout = [
    [sg.Input(key="p", size=50), sg.Button("Go")],
    [sg.Multiline(key="out", size=(70, 15))]
]

win = sg.Window("Summarize GPT", layout)
#Title of the window
while True:
    e, v = win.read()
    if e == sg.WINDOW_CLOSED: #closes the window
        break
    if e == "Go":
        r = client.responses.create(
            model="gpt-5.2",
            input=v["p"]
        ) #creates reponse after hitting Go
        win["out"].update(r.output_text) #response is created and shown to the GUI

win.close()
