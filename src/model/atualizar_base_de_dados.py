import logging as log
import gspread
import gspread_dataframe as gd
import pandas as pd

def atualizar_base_de_dados(dataframe):
    print('atualizando planilha online')
    log.info('atualizando planilha online')
    
    gc = gspread.service_account(filename='base_de_dados.json')
    sh = gc.open_by_key('1tXMfVw-MJpOhyjZvL5yZC8BHoNcQOFqOn6V7leRA5TE')

    worksheet = sh.sheet1

    df_online = pd.DataFrame(worksheet.get_all_records())
    
    df_todos_dados = pd.concat([df_online, dataframe])
    
    gd.set_with_dataframe(worksheet, df_todos_dados)
    
    print('planilha online atualizada')
    log.info('planilha online atualizada')