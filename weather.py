from base import chain_get

def get_weather(conffile='conf/weather.conf'):
    sect, conf, data = chain_get(conffile)
    name = None
    if conf is not None:
        name = conf.get('name')
    weather = None
    if data is not None:
        url = conf['url']
        if 'yytianqi' in url:
            weather = yytianqi(data)
        elif 'qweather' in url:
            weather = qweather(data)
        elif 'seniverse' in url:
            weather = seniverse(data)
    return {'vendor': name, 'data': weather}

def merge(k1, k2):
    res = k1
    if k1 != k2:
        res = res + ' - ' + k2
    return res


def yytianqi(data):
    def parse(day):
        tq = merge(day['tq1'], day['tq2'])
        fl = merge(day['fl1'], day['fl2'])
        fx = merge(day['fx1'], day['fx2'])
        qw = merge(day['qw2'], day['qw1'])
        date = day['date']
        return {
                'weather': tq,
                'wind_power': fl,
                'wind_dir': fx,
                'temperature': qw,
                'date': date
                }
    res = [parse(day) for day in data['data']['list']]
    return res

def qweather(data):
    def parse(day):
        date = day['fxDate']
        temp = merge(day['tempMin'], day['tempMax'])
        wind_dir = merge(day['windDirDay'], day['windDirNight'])
        wind_power = merge(day['windScaleDay'], day['windScaleNight'])
        weather = merge(day['textDay'], day['textNight'])
        return {
                'date': date,
                'temperature': temp,
                'wind_dir': wind_dir,
                'wind_power': wind_power,
                'weather': weather,
                }
    res = [parse(day) for day in data['daily']]
    return res

def seniverse(data):
    return 2

if '__main__' == __name__:
    print(get_weather('conf/weather.conf'))
