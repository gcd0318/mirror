import configparser
import json
import requests

def load_config(conffile='mirror.conf'):
    config = configparser.ConfigParser()
    config.read(conffile)
    sections = config.sections()
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
    return j

if '__main__' == __name__:
    conf = load_config()
    for sect in conf:
        if 'url' in conf[sect]:
            print(sect, get_data(conf, sect))
#    air = get_data(conf, 'air')
#    print(air)

#    weather = get_data(conf, 'weather')
#    print(weather)
