import configparser
from conf import *


# TODO: varibale formats need to be handled, currently everything is a string
def load_ini(path):
    config = configparser.ConfigParser()
    config.read(path)
    confs = {}
    for section in config.sections():
        confs[section] = {}
        for key, value in config.items(section):
            confs[section][key] = value

    # load settings
    settings.load_settings(**confs)
