#custom_logger.py
#Leonardo Duarte
import logging 
#Logging levels
INFO     = logging.INFO
DEBUG    =  logging.DEBUG
WARNING  = logging.WARNING
ERROR    = logging.ERROR
def setup(name, **kwargs):
    log_level=kwargs.get('log_level',INFO)
    formatter = logging.Formatter(fmt='%(asctime)s templatetool %(levelname)s: %(message)s', datefmt='%Y-%m-%d %I:%M:%S')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    logger.addHandler(handler)
    return logger

def dashed_line():
    print("----------------------------------------") 
def print_objects(**kwargs):
    log = logging.getLogger('main')
    if log.level == DEBUG:
        for k, v in kwargs.items():
            print(f'{k}:')
            print(f'{v}')
            log.debug(f'{k}:')
            dashed_line(f'{v}')

        

