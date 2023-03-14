import pyautogui as pyg
from time import sleep
import string
import random
import subprocess
subprocess.run(r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe')
excluded = []
letters = list(string.ascii_lowercase)
sleep(2)
for _ in range(10):
    for _ in range(len(letters)):
        choice = random.choice(letters)
        if choice not in excluded:
            pyg.hotkey('ctrl', 'l')
            pyg.press(choice)
            pyg.press('enter')
            excluded.append(choice)
            break
    sleep(1)
subprocess.call(['taskkill', '/IM', 'msedge.exe'])
