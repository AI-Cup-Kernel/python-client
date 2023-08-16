import requests

class Game:
    def __init__(self, token, server_ip, server_port) -> None:
        self.token = token
        self.server_ip = server_ip
        self.server_port = server_port
    
    def handel_output(self, response):
        code = response.status_code
        if 200<=code<300:
            return eval(response.text)
        try:
            print(response.json()['error'])
        except:
            print("unknown error")
        return dict()

    def get_owner(self):
        try:
            resp = requests.request('GET', f'http://{self.server_ip}:{self.server_port}/get_owners', headers={'x-access-token': self.token})
        except:
            print("can't make request")
            return
        return self.handel_output(resp)
    
    def get_number_of_troops(self):
        try:
            resp = requests.request('GET', f'http://{self.server_ip}:{self.server_port}/get_troops_count', headers={'x-access-token': self.token})
        except:
            print("can't make request")
            return
        return self.handel_output(resp)
    

    def get_state(self):
        try:
            resp = requests.request('GET', f'http://{self.server_ip}:{self.server_port}/get_state', headers={'x-access-token': self.token})
        except:
            print("can't make request")
            return

        return self.handel_output(resp)

    def get_turn_number(self):
        try:
            resp = requests.request('GET', f'http://{self.server_ip}:{self.server_port}/get_turn_number', headers={'x-access-token': self.token})
        except:
            print("can't make request")
            return
        return self.handel_output(resp)

