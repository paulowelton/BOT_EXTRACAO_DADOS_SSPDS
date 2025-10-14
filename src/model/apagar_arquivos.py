import os
import logging as log

def apagar_arquivos(arquivo):
    log.info(f'apagando arquivo: {arquivo}')
    print(f'apagando arquivo: {arquivo}')
    
    cam = f'C:\\Users\\{os.getlogin()}\\Downloads\\{arquivo}'
    
    if os.path.exists(cam):
        os.remove(cam)