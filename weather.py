from base import chain_get

def get_weather(conffile='conf/weather.conf'):
    sect, data = chain_get(conffile)
    name = None
    if sect is not None:
        name = sect.get('name')
    if data is not None:
        pass
    return {'vendor': name, 'data': data}

if '__main__' == __name__:
    print(get_weather('conf/weather.conf'))
