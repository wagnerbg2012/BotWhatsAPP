###################### Importação biblioteca ##################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time
import requests

#API 
agent = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

#CHAVE    TJmq3BXJK3Zh9YZoRQKmlrHlPEIlEeaK
api = requests.get("https://editacodigo.com.br/index/api-whatsapp/TJmq3BXJK3Zh9YZoRQKmlrHlPEIlEeaK" ,  headers=agent)
api = api.text
api = api.split(".n.")
bolinha_notificacao = api[3].strip()
contato_cliente = api[4].strip()
caixa_msg = api[5].strip()
msg_cliente = api[6].strip()
caixa_msg2 = api[7].strip()
caixa_pesquisa = api[8].strip()


###############################################################################################################################
#ler as pasta do sistema 
dir_path = os.getcwd()

#Salvar as sessão do navegador
chrome_options2 = Options()
chrome_options2.add_argument(r"user-data-dir=" + dir_path + "/pasta/sessao")
driver = webdriver.Chrome(options=chrome_options2)
#Acessar a sessão do whatsApp
driver.get('https://web.whatsapp.com/')
time.sleep(10)

#######################################################Criando bot########################################################################

def bot():
    try:
       bolinha = driver.find_element(By.CLASS_NAME,bolinha_notificacao)
       bolinha = driver.find_elements(By.CLASS_NAME,bolinha_notificacao)
       clica_bolinha = bolinha[-1] 
       acao_bolinha = webdriver.common.action_chains.ActionChains(driver)
       acao_bolinha.move_to_element_whit_offset(clica_bolinha,0,-20)
       acao_bolinha.click()
       acao_bolinha.perform()
       acao_bolinha.click() 
       acao_bolinha.perform()

       # x1rg5ohu x173ssrc x1xaadd7 x682dto x1e01kqd x12j7j87 x9bpaai x1pg5gke x1s688f xo5v014 x1u28eo4 x2b8uid x16dsc37 x18ba5f9 x1sbl2l xy9co9w x5r174s x7h3shv
        #fça isso aqui
        #caso não consiga , tenta uma outra coisa
    except:
        #Entao vou tentar isoo aqui
       print('ola')
while True:
    bot()

       
