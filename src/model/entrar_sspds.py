import traceback
import logging as log
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def entrar_sspds(navegador):
    try:
        log.info("Entrando no sspds")
        print("Entrando no sspds")

        

        # entrando no site do sspds
        navegador.get("https://www.sspds.ce.gov.br/indicadores-de-seguranca-publica/")
        navegador.maximize_window() 

    except:
        msg_erro = traceback.format_exc()
        
        log.info(f"Houve um erro na funcao de entrar no sspds: {msg_erro}")
        print(f"Houve um erro na funcao de entrar no sspds: {msg_erro}")