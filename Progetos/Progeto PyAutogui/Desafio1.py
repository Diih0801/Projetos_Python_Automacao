# DESAFIO 1
import pyautogui
import webbrowser
from time import sleep

# 1) Navegue até o site https://cursoautomacao.netlify.app/.
webbrowser.open('https://cursoautomacao.netlify.app/')
sleep(0.9)
# 2) Encontre e clique no campo "Digite seu nome" dentro de "Exemplos
# Alertas" e digitar seu nome.
pyautogui.moveTo(1172,190,duration=0.5)
pyautogui.scroll(-700)
sleep(1)
pyautogui.click(1042,529,duration=0.2)
pyautogui.typewrite('Diego Gomes de Oliveira')
# 3) Clicar em alerta, para gerar a alerta.
pyautogui.click(1011,568,duration=0.2)
# 4) Feche o alerta.
pyautogui.click(827,175,duration=0.5)
# 5) Suba a página totalmente para cima.
pyautogui.scroll(700)
sleep(1.5)
# 6) Desça apenas o suficiente para conseguir chegar até a secção
# que contem os arquivos para o qual você ira faer o download deles
# e clicar e movimentar o mouse da maneira que for necessária para 
# os arquivos EXCEL e PDF.
pyautogui.scroll(-1900)
pyautogui.click(193,532,duration=0.3)
sleep(1.5)
pyautogui.click(368,531,duration=0.3)
# 7) Depois de ter feito isso eu quero que você crie um alerta que diz 
# "VOCÊ TERMINOU!".
pyautogui.alert(text='VOCÊ TERMINOU!',title='Automação de Sites')
