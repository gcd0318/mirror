import configparser
import json
import requests

def load_config(conffile):
    config = configparser.ConfigParser()
    config.read(conffile)
#    sections = config.sections()
    for sect in config:
        section = config[sect]
    return config

def get_data(config, infoname, **kwargs):
    conf = config[infoname]
    for k in kwargs:
        if k in conf:
            conf[k] = kwargs[k]
    url = conf['url']
    for k in conf:
        if 'url' != k:
            url = url.replace('{' + k  + '}', conf[k])
    resp = requests.get(url)
    j = None
    if 200 == resp.status_code:
        j = json.loads(resp.text)
        if conf.get('ok_code') != str(j.get('code')):
            j = None
    return j

def chain_get(conffile):
    config = load_config(conffile)
    sections = config.sections()
    j = None
    i = 0
    sect = None
    while (i < len(config)) and (j is None):
        sect = sections[i]
        j = get_data(config, sect)
        i = i + 1
    if i < len(config):
        conf = config[sect]
    else:
        conf = None
    return sect, conf, j

if '__main__' == __name__:
    conffile = 'conf/mirror.conf'
    conf = load_config(conffile)
    for sect in conf:
        if 'url' in conf[sect]:
            print(sect, get_data(conf, sect))
