import traceback
import logging as log
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep
import os

def baixar_relatorios(navegador, relatorio):
    try: 
        container_relatorios = WebDriverWait(navegador, 180).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div/div/section[2]")))
        navegador.execute_script("arguments[0].scrollIntoView(true);", container_relatorios)
        
        btns_relatorios = container_relatorios.find_elements(By.TAG_NAME, 'li')
    
        for btn_relatorio in btns_relatorios:
            
            titulo = btn_relatorio.find_element(By.TAG_NAME, 'h3').text
            
            if titulo == relatorio:
                btn_relatorio.click()
                
                while True:
                    arquivo = f"C:\\Users\\{os.getlogin()}\\Downloads\\{titulo.capitalize()}_2009-a-2024.xlsx"

                    if os.path.exists(arquivo):
                        break
                    else:
                        sleep(1)
        
    except:
        msg_erro = traceback.format_exc()
        
        log.info(f"Houve um erro na funcao de baixar relatorios: {msg_erro}")
        print(f"Houve um erro na funcao de baixar relatorios: {msg_erro}")