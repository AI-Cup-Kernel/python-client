import json
import requests
from flask import Flask

# read config file from config.json
config = json.load(open('config.json'))
server_ip = config['server_ip']
server_port = config['server_port']

# make a login request to the server 
try:
    login_response = requests.request('GET', f'http://{server_ip}:{server_port}/login').json()
except:
    print("the server is not running")
    exit()


try:
    id = login_response['player_id']
    token = login_response['token']
    my_port = login_response['port']
except:
    print('server is full')
    exit()



# make a server to get the start of my turn
app = Flask(__name__)


def ready():
    resp = requests.request('GET', f'http://{server_ip}:{server_port}/ready', headers={'x-access-token': token})
    code = resp.status_code
    if 200<=code<300:
        print('ready')
    else:
        print("can't make a ready request")
        exit()

with app.app_context():
    ready()

app.run(debug=True, port=my_port, use_reloader=False)

