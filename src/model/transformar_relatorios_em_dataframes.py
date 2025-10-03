import traceback
import logging as log
import pandas as pd
import os

from list_relatorios import relatorios

def transformar_relatorios_em_dataframes():
    
    try:
        for relatorio in relatorios:
            log.info(f"Transformando relatorio de {relatorio} em dataframe")
            print(f"Transformando relatorio de {relatorio} em dataframe")
            
            arquivo_xlsx = f"C:\\Users\\{os.getlogin()}\\Downloads\\{relatorio.capitalize()}_2009-a-2024.xlsx"

            dataframe = pd.read_excel(arquivo_xlsx)
            
            print(dataframe)
            
    except:
        msg_erro = traceback.format_exc()
        
        log.error(f"Houve um erro na funcao de transformar relatorios em dfs: {msg_erro}")
        print(f"Houve um erro na funcao de transformar relatorios em dfs: {msg_erro}")
        
if __name__ == '__main__':
    transformar_relatorios_em_dataframes()