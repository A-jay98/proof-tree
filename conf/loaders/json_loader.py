from json import load
from conf import *


def load_json(path):
    with open(path, 'r') as (f):
        confs = load(f)
    settings.load_settings(**confs)
