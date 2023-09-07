import pyautogui
from time import sleep

# Entrar no site Brasil
pyautogui.click(829,746,duration=0.2)
pyautogui.click(488,54,duration=0.2)
pyautogui.typewrite('https://pt.wikipedia.org/wiki/Brasil')
pyautogui.press('enter')
# Descer até a secção de História
pyautogui.moveTo(573,429,duration=0.2)
sleep(3)
for i in range(20):
    pyautogui.scroll(-100)
