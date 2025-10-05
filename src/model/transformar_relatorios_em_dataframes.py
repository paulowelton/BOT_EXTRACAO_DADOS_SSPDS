import os
import traceback
import pandas as pd
import logging as log
from datetime import datetime

# from  list_relatorios import relatorios

relatorios = [
    'FURTO'
]

def transformar_relatorios_em_dataframes(relatorio):
    
    try:
        
        log.info(f"Transformando relatorio de {relatorio} em dataframe")
        print(f"Transformando relatorio de {relatorio} em dataframe")
            
        arquivo_xlsx = f"C:\\Users\\{os.getlogin()}\\Downloads\\{relatorio.capitalize()}_2009-a-2024.xlsx"

        dataframe = pd.read_excel(arquivo_xlsx)

        dataframe['Data'] = pd.to_datetime(dataframe['Data'])

        data_minima = datetime(year=2020, month=1, day=1)

        dataframe = dataframe[dataframe['Data'] > data_minima]   

        dataframe['Tipo'] = relatorio.capitalize()

        return dataframe
            
    except:
        msg_erro = traceback.format_exc()
        
        log.error(f"Houve um erro na funcao de transformar relatorios em dfs: {msg_erro}")
        print(f"Houve um erro na funcao de transformar relatorios em dfs: {msg_erro}")
        
if __name__ == '__main__':
    transformar_relatorios_em_dataframes()