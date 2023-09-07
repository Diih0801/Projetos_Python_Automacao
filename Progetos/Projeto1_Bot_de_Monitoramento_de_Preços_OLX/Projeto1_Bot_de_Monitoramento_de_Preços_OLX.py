from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By # Para encontrar elementos importar By.
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

def iniciar_driver():

    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs',{
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver

#driver = webdriver.Chrome()
driver = iniciar_driver()
# Navegar até o site
driver.get('https://www.olx.com.br/videogames/estado-sp/sao-paulo-e-regiao/centro?q=xbox%20one')
while True:
    sleep(70)
    # Carregar todos elementos da tela movendo até o final da página e depois ao topo.
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
    sleep(10)
    # Encontrar os títulos
    titulos = driver.find_elements(By.XPATH,'//div[@class="sc-gVkuDy ctkhqx horizontal"]')
    # Encontrar os preços
    precos = driver.find_elements(By.XPATH,'//h3[@class="sc-pVTFL fFnpzY horizontal  price"]')
    # Encontrar os links
    links = driver.find_elements(By.XPATH,'//a[@class="sc-gXRojI ebUwTH"]')
    # Guardar em um arquivo .csv
    for titulo, preco, link in zip(titulos,precos,links):
        with open('Precos_XboxOne_OLX.csv','a',encoding='utf-8',newline='') as arquivo:
            link_processado = link.get_attribute('href') # Para extrair o link.
            arquivo.write(f'{titulo.text};{preco.text};{link_processado}{os.linesep}') # os.linesep é para pular a linha
    # Fazer isso para todas as páginas existentes                                      # e ficar um embaixo do outro
    try:
        botao_proxima_pagina = driver.find_element(By.XPATH,"//span[text()='Próxima página']")
        sleep(5)
        botao_proxima_pagina.click()
    except:
        print('Chegamos na última página!')
        break

input('')
driver.close()
