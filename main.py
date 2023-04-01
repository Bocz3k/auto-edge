import pyautogui as pyg
from time import sleep
import string
import random
import subprocess
print("Running!")
print("Please don't click during the process\n")
subprocess.run(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
print("Starting to open Microsoft Edge")
excluded = []
excluded2 = []
letters = list(string.ascii_letters)
sleep(0.5)
print("Microsoft Edge opened")
for _ in range(67):
    for _ in range(len(letters)):
        choice = random.choice(letters)
        choice2 = random.choice(letters)
        if choice not in excluded and choice2 not in excluded2:
            pyg.hotkey('ctrl', 'l')
            pyg.press(choice)
            pyg.press(choice2)
            pyg.press('enter')
            print(f"Succesfully entered: {choice}{choice2}")
            excluded.append(choice)
            excluded2.append(choice2)
            sleep(0.1)
            break
print("Terminating Microsoft Edge")
subprocess.call(['taskkill', '/IM', 'msedge.exe'])
