import logging
import pathlib
from datetime import datetime
# Creamos el directorio 'logs' si no existe
audit_dir = pathlib.Path('logs')
audit_dir.mkdir(exist_ok=True)
# Creamos archivo de log dentro del directorio 'logs'
log_file = audit_dir / f'suite_{datetime.now().strftime("%Y-%m-%d")}.log'
# Configuramos el logger
logger = logging.getLogger('Talento Tech Automation')
logger.setLevel(logging.INFO)
# Configuramos el manejador de archivo
if not logger.handlers:
    # Formato del log
    # Modo de apertura 'a' para append(agregar) y codificación 'utf-8'
    file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
    # Defino variable para el formateador
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                datefmt='%Y-%m-%d %H:%M:%S'
                            )
    # Asigno el formateador al manejador de archivo
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    # Handler a consola para pytest
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)