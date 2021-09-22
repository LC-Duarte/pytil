#custom_logger.py
#Leonardo Duarte
import logging 
import multiprocessing as mp
#import facilities.c_globals as g
import os
#Logging levels
INFO     = logging.INFO
DEBUG    =  logging.DEBUG
WARNING  = logging.WARNING
ERROR    = logging.ERROR
FORMATTER = logging.Formatter(fmt='%(asctime)s ' + 'PROTOTYPE' +' %(filename)s:%(lineno)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %I:%M:%S')
def setup(name, **kwargs):
    log_level=kwargs.get('log_level',INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(FORMATTER)
    logger = logging.getLogger(name)
    #logger = mp.get_logger(name)
    logger.setLevel(log_level)
    logger.addHandler(handler)
    return logger

def set_output(logger, **kwargs):
    log_path = kwargs.get('log_path', 'hispger.log')
    log_level= kwargs.get('log_level', logging.INFO)
    if log_path != None:
        if os.path.isfile(log_path):
            os.remove(log_path)
        else:
            file = open(log_path, 'w+')
        fh = logging.FileHandler(log_path)
        fh.setLevel(log_level)
        fh.setFormatter(FORMATTER)
        logger.addHandler(fh)

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
        out += str(x)
        log.debug(out)
        c += 1
        if c == limit:
            break
    dashed_line()
