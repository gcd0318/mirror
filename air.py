from base import chain_get

def get_air(conffile='conf/air.conf', i=-1):
    sect, conf, data = chain_get(conffile, i)
    name = None
    if conf is not None:
        name = conf.get('name')
    air = None
    if data is not None:
        url = conf['url']
        if 'juheapi' in url:
            air = juheapi(data)
    return {'vendor': name, 'data': air}

def juheapi(data):
    def parse(air):
        city = air['city']
        overall = air['aqi']
        pm10 = air['pm10']
        pm25 = air['pm25']
        o3 = air['o3']
        return {
                'city': city,
                'overall': overall,
                'pm10': pm10,
                'pm25': pm25,
                'o3': o3,
                }
    return parse(data['data'])

if '__main__' == __name__:
    print(get_air())
