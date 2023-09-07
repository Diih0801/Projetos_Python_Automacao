# Alertar e pedir informação no PyAutogui
import pyautogui

pyautogui.alert(text='Iniciando sua automação',
                title='Automação de Login',
                button='ok')

# Pedir informação e-mail e senha
email = pyautogui.prompt(text='Digite seu e-mail',
                         title='Informações obrigatorias')
senha = pyautogui.password(text='Digite sua senha:',
                           title='Informações obrigatorias',
                           mask='*')
print(f'Você digitou o e-mail: {email}')
print(f'Você digitou a senha: {senha}')
# Passar informação do e-maile senha para um bloco de notas
pyautogui.click(863,172,duration=0.5)
pyautogui.typewrite(f'E-mail: {email}')
pyautogui.press('enter')
pyautogui.typewrite(f'Senha: {senha}')

# Confirmar se algo deve ou não acontecer
resposta = pyautogui.confirm(text='Continuar rodando nossa automção?',
                             title='confirmação',buttons=['sim','não','cancelar'])
if resposta == 'sim':
    print('continuando automação')
elif resposta == 'não':
    print('Encerrando automação')
else:
    print('operção cancelada')
