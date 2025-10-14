import traceback
import logging as log
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os

relatorios = [
    'FURTO',
    'CRIMES SEXUAIS',
    'LEI 11.340/06 (LEI MARIA DA PENHA)',
    'HOMOFOBIA E TRANSFOBIA',
    'CRIME OU PRECONCEITO DE RAÇA OU DE COR',
    'CRIMES VIOLENTOS LETAIS E INTENCIONAIS – CVLI',
    'CRIMES VIOLENTOS CONTRA O PATRIMÔNIO – CVP',
    'INDÍGENAS VÍTIMAS DE CRIMES'
]

def baixar_relatorios():
    
    relatorios_baixados = []
    
    def aguardar_arquivo_baixar(nome_arquivo):
        while True:
            if os.path.exists(f'C:\\Users\\{os.getlogin()}\\Downloads\\{nome_arquivo}'):
                break
            else:
                print('aguardando relatorio baixar', nome_arquivo)
                sleep(1)
    
    try: 
        log.info("Entrando no sspds")
        print("Entrando no sspds")
        
        navegador = webdriver.Chrome()

        # entrando no site do sspds
        navegador.get("https://www.sspds.ce.gov.br/indicadores-de-seguranca-publica/")
        navegador.maximize_window() 
        
        
        # rolando ate o container onde tem os relatorios necessarios
        container_relatorios = WebDriverWait(navegador, 180).until(EC.presence_of_element_located((By.XPATH, "/html/body/main/section/div/div/section[2]")))
        navegador.execute_script("arguments[0].scrollIntoView(true);", container_relatorios)
        
        # array com todos os botoes que baixam os relatorios
        btns_relatorios = container_relatorios.find_elements(By.TAG_NAME, 'li')
        
        
        for relatorio in relatorios:
            log.info(f'Baixando relatorio de {relatorio}')
            print(f'Baixando relatorio de {relatorio}')
            
            for btn_relatorio in btns_relatorios:
                
                titulo = btn_relatorio.find_element(By.TAG_NAME, 'h3').text
                
                if titulo == relatorio:
                    btn_relatorio.click()
                    
                    a = btn_relatorio.find_element(By.TAG_NAME, 'a')
                    
                    href = a.get_attribute('href')
                    
                    nome_arquivo = href.split('/')[-1]
                    
                    relatorios_baixados.append(nome_arquivo)
                    
                    aguardar_arquivo_baixar(nome_arquivo)
        
        return relatorios_baixados
    except:
        
        msg_erro = traceback.format_exc()
        
        log.info(f"Houve um erro na funcao de baixar relatorios: {msg_erro}")
        print(f"Houve um erro na funcao de baixar relatorios: {msg_erro}")
        
if __name__ == '__main__':
    baixar_relatorios()