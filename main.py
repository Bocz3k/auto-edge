import pyautogui as pyg
from time import sleep
import string
import random
import subprocess
print("Running!\n")
subprocess.run(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
print("Starting to open Microsoft Edge")
excluded = []
letters = list(string.ascii_lowercase)
sleep(2)
print("Microsoft Edge opened")
for _ in range(11):
    for _ in range(len(letters)):
        choice = random.choice(letters)
        if choice not in excluded:
            pyg.hotkey('ctrl', 'l')
            pyg.press(choice)
            pyg.press('enter')
            print(f"Succesfully entered letter [{choice.upper()}]")
            excluded.append(choice)
            break
    sleep(1)
print("Terminating Microsoft Edge")
subprocess.call(['taskkill', '/IM', 'msedge.exe'])
