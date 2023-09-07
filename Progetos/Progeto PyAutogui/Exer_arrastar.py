import pyautogui

for i in range(10):
    # Mover o mouse
    pyautogui.moveTo(963,195,duration=1.1)
    # Pegar o arquivo mover e soltar
    pyautogui.dragTo(933,590,button='left',
    duration=1.1)
