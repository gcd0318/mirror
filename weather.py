from base import chain_get

def get_weather(conffile='weather.conf'):
    sect, data = chain_get(conffile)
    print(data)

if '__main__' == __name__:
    print(get_weather())
