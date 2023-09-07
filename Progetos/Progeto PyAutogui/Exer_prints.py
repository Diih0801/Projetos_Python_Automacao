# Como tirar print(foto) da tela inteira ou parte dela
import pyautogui as pg
# Print da tela inteira
pg.screenshot('tela.jpg')
# Print de parte da tela
pg.screenshot('calculadora.jpg', 
              region=(1001,94,320,535))
