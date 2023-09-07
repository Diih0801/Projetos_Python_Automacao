# Reconhecimento de imagem simples com pyautogui
import pyautogui
# Encontrar as cordenadas próximas de onde a imagem está
print(pyautogui.locateOnScreen('numero4.png'))
# Encontrar a coordenada do centro da imagem
# coloquei a localização da imagem em uma variavel.
codernada_centro =pyautogui.locateCenterOnScreen('numero4.png')
# como clicar na imagem (com uma variavel)
pyautogui.click(codernada_centro, duration=2)
