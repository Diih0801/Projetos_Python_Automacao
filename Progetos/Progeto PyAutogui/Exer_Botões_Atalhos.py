# Como usar Botões e atalhos do teclado
import pyautogui
from time import sleep

# Para ver todos possíveis teclas, rode código abaixo:
# print(pyautogui.KEYBOARD_KEYS)
# pyautogui.press('win')
# pyautogui.typewrite('Excel')
# sleep(1)
# pyautogui.press('enter')

# Como usar combinações de teclas
# Entrar na conta
pyautogui.click(1158,96,duration=0.5)
sleep(0.8)
pyautogui.scroll(-100)
# Pegar e-mail e senha
pyautogui.click(818,495,duration=0.5)
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('ctrl','c')
pyautogui.click(1062,225,duration=0.5)
pyautogui.hotkey('ctrl','v')
