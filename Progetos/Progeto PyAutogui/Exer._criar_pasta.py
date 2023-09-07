import pyautogui

# Abrir local da nova pasta.
pyautogui.doubleClick(x=1160,y=37,duration=1.5)

# Clicar com o botão direito 
pyautogui.rightClick(x=618,y=405,duration=1.5)

# Mover o mouse e clicar em (Mostrar mais opções)
pyautogui.move(30,0, duration=1.5)
pyautogui.move(0,20, duration=1.3)
pyautogui.click()

# Mover o mouse para o item (novo)
pyautogui.move(50,0, duration=1.5)
pyautogui.move(0,250, duration=1.2)

# Mover o mouse e clicar (Pasta)
pyautogui.move(310,0, duration=1.5)
pyautogui.move(0,-214, duration=1.2)
pyautogui.click()
pyautogui. typewrite('Pasta Concluida')

