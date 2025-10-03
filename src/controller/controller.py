import traceback
import logging as log

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

    
    
except:
    msg_erro = traceback.format_exc()
    
    log.error(f"Houve um erro no controller: {msg_erro}")
    print(f"Houve um erro no controller: {msg_erro}")

finally:
    log.info("Final do programa")
    print("Final do programa")
    