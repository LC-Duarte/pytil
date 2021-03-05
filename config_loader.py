#config_loader.py
#Leonardo duarte
import yaml
import os
import logging  
log = logging.getLogger('main')


def load_config_file(**kwargs):
    """
    Loads configuration file
    path - named argument specifies the path for the config file
    if no path is specified it will look for config.yaml under de current directory
    returns the parsed yaml as dictionary
    """
    file_path = kwargs.get('path', os.path.join(os.getcwd(),"config.yaml"))
    with open(file_path, "r",encoding='utf8') as ymlfile:
        try:
            yaml_file = yaml.safe_load(ymlfile)
            config = yaml_file if yaml_file != None else config
            if yaml_file == None:
                log.error('Failed to load configuration')
                return None
        except:
            log.error('No config file on '+ file_path)
            return None         
    return config  