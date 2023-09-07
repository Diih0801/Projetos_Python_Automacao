import pyautogui
import pyperclip
from time import sleep
# Abrir whats no navegador

# Função para adcionar caracteres especiais nas msg.
def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')


pyautogui.click(952,24,duration=0.5)
sleep(3)
pyautogui.click(928,62,duration=0.5)
pyautogui.typewrite('https://web.whatsapp.com/')
pyautogui.press('enter')
sleep(10)
# Procurar grupo ou pessoa 
pyautogui.click(841,197,duration=0.5)
pyautogui.typewrite('Estudo de Python')
pyautogui.click(854,327,duration=0.5)
# Escrever mensagem
pyautogui.click(1186,681,duration=0.5)
escrever_frase('Olá, Boa noite teste PYTHON !!!') # Função
# pyautogui.typewrite('Olá, boa noite teste PYTHON !!!')
pyautogui.press('enter')
