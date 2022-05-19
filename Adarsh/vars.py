# (c) adarsh-goel

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    MULTI_CLIENT = False
    API_ID = 3325855
    API_HASH = "a0ee8fbebe1950b9291c9e22da4a1450"
    BOT_TOKEN = "5125608381:AAHvqaloaaUaT1DNUa2rYcjQel_GC3RwCLs"
    SESSION_NAME = 'filetolinkbot'
    SLEEP_THRESHOLD = '30'
    WORKERS = '4'
    BIN_CHANNEL = -1001783123841
    PORT = 8080
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = "1200"  # 20 minutes
    OWNER_ID =  1089528685
    NO_PORT = False
    APP_NAME = None
    OWNER_USERNAME = "S4tyendra"
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = "mongodb+srv://satya:s4tya@cluster0.rrqhs.mongodb.net/utyfky?retryWrites=true&w=majority"
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
