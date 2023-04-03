import pyautogui as pyg
from time import sleep
import string
import random
import subprocess
from colored import fg
VERSION = 1.2

def print2(state, text):
    if state == 'info': print(fg('steel_blue_3') + "[INFO] " + fg('white') + text)
    elif state == 'warn': print(fg('orange_1') + "[WARN] " + fg('white') + text)
    elif state == 'error': print(fg('light_red') + "[ERROR] " + fg('white') + text)

print2('info', "Running version " + fg('purple_1b') + f"{VERSION}" + fg('white') + "!")
print2('warn', "Please don't click during the process\n")
subprocess.run(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
print2('info', "Starting to open Microsoft Edge")

excluded = []
excluded2 = []
letters = list(string.ascii_letters)
sleep(0.5)
print2("info", "Microsoft Edge opened")

for _ in range(67):
    for _ in range(len(letters)):
        choice = random.choice(letters)
        choice2 = random.choice(letters)
        if choice not in excluded and choice2 not in excluded2:
            pyg.hotkey('ctrl', 'l')
            pyg.press(choice)
            pyg.press(choice2)
            pyg.press('enter')
            print2('info', f"Succesfully entered: {choice}{choice2}")
            excluded.append(choice)
            excluded2.append(choice2)
            sleep(0.1)
            break

print2('info', "Terminating Microsoft Edge")
subprocess.call(['taskkill', '/IM', 'msedge.exe'])
