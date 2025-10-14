import traceback
import logging as log

from src.model.baixar_relatorios import baixar_relatorios
from src.model.transformar_relatorios_em_dataframes import transformar_relatorios_em_dataframes
from src.model.atualizar_base_de_dados import atualizar_base_de_dados

# limpando o log
with open("log.txt", "w") as file:
    pass

# configurando o log
log.basicConfig(filename="log.txt",
                level=log.INFO,
                format="%(asctime)s - %(levelname)s - %(message)s",
                datefmt="%d/%m/%Y %I:%M:%S %p")

try:
    log.info("Inicio do programa")
    print("Inicio do programa")

    relatorios = baixar_relatorios()
    
    for relatorio in relatorios:
        
        df = transformar_relatorios_em_dataframes(relatorio)

        atualizar_base_de_dados(df, relatorio)
    
except:
    msg_erro = traceback.format_exc()
    
    log.error(f"Houve um erro no controller: {msg_erro}")
    print(f"Houve um erro no controller: {msg_erro}")

finally:
    log.info("Final do programa")
    print("Final do programa")
    