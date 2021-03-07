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
    log = logging.getLogger('main')
    line = "----------------------------------------"
    log.debug(line)
def print_objects(**kwargs):
    log = logging.getLogger('main')
    for k, v in kwargs.items():
        log.debug(f'{k}:')
        log.debug(f'{v}')
        dashed_line()

        
def print_list(list, **kwargs):
    log = logging.getLogger('main')
    bullet = kwargs.get("bullet", True)
    tab = kwargs.get('tab', True)
    limit = kwargs.get('limit', -1)
    name = kwargs.get('name', None)
    c = 0
    if name != None:
        log.debug(f'{name}:')
    for x in list:
        out = ''
        if tab:
            out += '\t'
        if bullet:
            out += '* '
        out += x
        log.debug(out)
        c += 1
        if c == limit:
            break
    dashed_line()
