# Bot de curtidas e comentários no Instagram com PyAutoGUI
import webbrowser
import pyautogui
from time import sleep


def sair():
    pyautogui.click(1263,97,duration=1)
    sleep(0.5)
    pyautogui.click(42,672,duration=1)
    sleep(0.5)
    pyautogui.click(40,617,duration=1)
    sleep(0.5)
    pyautogui.click(1342,13,duration=1)


# 1 - Navegar até o site https://www.instagram.com
while True:
    webbrowser.open('https://www.instagram.com')
    sleep(5)
    # 2 - Entrar com o meu usuário 
    # (como o meu usuário ja estava logado só precisei clicar no botão para manter-se logado)
    login = pyautogui.locateCenterOnScreen('conta_logada.png')
    pyautogui.click(login[0],login[1],duration=1)
    sleep(4)
    # 3 - Pesquisar pela página
    pesquisa = pyautogui.locateCenterOnScreen('pesquisa.png')
    pyautogui.click(pesquisa[0],pesquisa[1],duration=1)
    pyautogui.typewrite('paamcavalcantii')
    pyautogui.move(85,0,duration=0.8)
    pyautogui.click()
    sleep(3)
    # 4 - Clicar na postagem mais recente
    pyautogui.moveTo(561,374,duration=1)
    sleep(2)
    pyautogui.scroll(-300)
    pyautogui.click(539,527,duration=1)
    sleep(1)
    # 5 - Verificar se já curti ou não aquela postagem
    nao_curtido = pyautogui.locateCenterOnScreen('nao_curtido.png')
    curtido = pyautogui.locateCenterOnScreen('curtido.png')
    # 6 - Se não tiver curtido, curtir a foto
    if nao_curtido:
        pyautogui.click(nao_curtido[0],nao_curtido[1],duration=1)
        # 7 - Se não tiver curtido, comentar a foto
        comentario = pyautogui.locateCenterOnScreen('comentario.png')
        pyautogui.click(comentario[0],comentario[1],duration=1)
        pyautogui.typewrite('Te amo!')
        sleep(3)
        pyautogui.click(1021,669,duration=0.6) # Botão para publicar
        # 8 - Após as 24 horas rodar de novo
        sair()
        sleep(30)
    # 9 - Se ja tiver curtido, fazer nada, e pausar o bot por 24 horas
    elif curtido:
        # 10 - Pausar por 24 horas    
        sair()
        sleep(30)
     