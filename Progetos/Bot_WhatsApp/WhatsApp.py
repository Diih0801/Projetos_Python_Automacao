'''QUAIS PASSOS MANUAIS PRECISO FAZER PARA ENVIAR UMA MENSAGEM.

1 - LISTA DE NÚMEROS
2 - ENVIAR INDIVIDUALMENTE UMA MENSAGEM PARA CADA PESSOA
3 - PAUSAR ENTRE CADA ENVIO

1.1 - ESCOLHER UM CONTATO 
2.1 - ENVIAR MENSAGEM PARA ESSE CONTATO 
        https://api.whatsapp.com/send?phone=TELEFONE DE QUEM VAI ENVIAR A MENSAGEM'''
import webbrowser
import pyautogui
from time import sleep

telefones = []

with open('lista_telefones.txt','r') as arquivo:
    for linha in arquivo:
        telefones.append(linha.split('\n')[0])
    print(telefones)

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(6)
    iniciar_conversa = pyautogui.locateCenterOnScreen('iniciar_conversa.png')
    pyautogui.click(iniciar_conversa[0],iniciar_conversa[1],duration=1)
    sleep(3)
    pyautogui.click(764,197,duration=1)
    sleep(8)
    pyautogui.click(639,696,duration=1)
    sleep(2)
    pyautogui.typewrite('Mensagem Teste Curso Python')
    sleep(1)
    pyautogui.press('enter')
    sleep(40)
