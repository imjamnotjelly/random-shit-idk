import pyautogui
from time import sleep

with open('shrek.txt', 'r') as file:
    shrek = file.read().replace('\n', '')

sleep(3)
for w in shrek.split():
    pyautogui.write(f'@bea_sunflower {w}')
    pyautogui.press('enter')
    sleep(2)


