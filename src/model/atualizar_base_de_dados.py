import logging as log
import gspread
import gspread_dataframe as gd
import pandas as pd

def atualizar_base_de_dados(dataframe, relatorio):
    print('atualizando planilha online')
    log.info('atualizando planilha online')
    
    pagina_procurada = str(relatorio.split('_')[0]).replace('-', ' ')
    
    gc = gspread.service_account(filename='base_de_dados.json')
    sh = gc.open_by_key('1tXMfVw-MJpOhyjZvL5yZC8BHoNcQOFqOn6V7leRA5TE')

    worksheet = None
    
    for ws in sh.worksheets():
    
        if ws.title.lower() == pagina_procurada.lower():
            worksheet = ws
            break
            
    if worksheet is None:
        print(f"Erro: Planilha '{pagina_procurada}' não encontrada no arquivo.")
        log.error(f"Erro: Planilha '{pagina_procurada}' não encontrada no arquivo.")
        return

    df_online = pd.DataFrame(worksheet.get_all_records())
    
    df_todos_dados = pd.concat([df_online, dataframe], ignore_index=True)
    
    gd.set_with_dataframe(worksheet, df_todos_dados)
    
    print('planilha online atualizada')
    log.info('planilha online atualizada')