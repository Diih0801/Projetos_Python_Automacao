# bot para jogar Guitar Flash.
import pyautogui
import keyboard
from time import sleep

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(924,645,(0,152,0)):
        pyautogui.press('a')
        sleep(0.02)
    if pyautogui.pixelMatchesColor(1015,642,(255,0,0)):
        pyautogui.press('s')
        sleep(0.02)
    if pyautogui.pixelMatchesColor(1105,644,(244,244,2)):
        pyautogui.press('j')
        sleep(0.02)
