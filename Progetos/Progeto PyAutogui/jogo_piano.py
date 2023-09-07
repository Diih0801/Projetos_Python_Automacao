# Automatizar jogo do Magic piano
import pyautogui
import keyboard
import win32api
import win32con
from time import sleep

# Clicar em START para começar
pyautogui.click(1012,411,duration=1)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)


while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(911,357,(0,0,0)):
        click(911,357)
    if pyautogui.pixelMatchesColor(981,350,(0,0,0)):
        click(981,350)
    if pyautogui.pixelMatchesColor(1048,351,(0,0,0)):
        click(1048,351)
    if pyautogui.pixelMatchesColor(1122,351,(0,0,0)):
        click(1122,351)
