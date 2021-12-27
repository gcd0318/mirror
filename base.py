import configparser
import logging
import json
import requests

def log(logname):
    logger = logging.getLogger(logname)
    if not logname.endswith('.log'):
        logname = '/var/log/mirror/' + logname + '.log'
    fh = logging.handlers.TimedRotatingFileHandler(logname, "D", 1, 10)
    fh.setFormatter(logging.Formatter('%(asctime)s %(filename)s_%(lineno)d: [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S'))
    logger.addHandler(fh)
    f = logging.Filter()
    logger.setLevel(logging.DEBUG)
    return logger

def load_config(conffile):
    config = configparser.ConfigParser()
    config.read(conffile)
#    sections = config.sections()
    for sect in config:
        section = config[sect]
    return config

def get_mirror(conffile):
    conf = load_config(conffile)
    return conf

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
        if str(conf.get('ok_code')) != str(j.get('code')):
            j = None
    return j

def chain_get(conffile, index=-1):
    config = load_config(conffile)
    sections = config.sections()
    i = 0
    m = len(sections)
    if (-1 < index) and (index < m):
        i = index
        m = index + 1
    j = None
    sect = None
    while (i < m) and (j is None):
        sect = sections[i]
        j = get_data(config, sect)
        i = i + 1
    conf = None
    if j is not None:
        conf = config[sect]
    return sect, conf, j

if '__main__' == __name__:
    conffile = 'conf/mirror.conf'
    conf = load_config(conffile)
    for sect in conf:
        if 'url' in conf[sect]:
            print(sect, get_data(conf, sect))
