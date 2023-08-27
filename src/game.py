import requests

class Game:
    def __init__(self, token, server_ip, server_port) -> None:
        self.token = token
        self.server_ip = server_ip
        self.server_port = server_port
        self.my_turn = False
    
    def handel_output(self, response):
        code = response.status_code
        if 200<=code<300:
            return eval(response.text)
        if 'error' in response.json():
            print(response.json()['error'])
            raise Exception(response.json()['error'])
        else:
            print("unknown error")
            raise Exception("unknown error")
        
    def get_owners(self):
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

    def get_adj(self):
        try:
            resp = requests.request('GET', f'http://{self.server_ip}:{self.server_port}/get_adj', headers={'x-access-token': self.token})
        except:
            print("can't make request")
            return
        return self.handel_output(resp)
    
    def next_state(self):
        try:
            resp = requests.request('GET', f'http://{self.server_ip}:{self.server_port}/next_state', headers={'x-access-token': self.token})
        except:
            print("can't make request")
            return
        return self.handel_output(resp)
    
    def put_one_troop(self, node_id):
        body = {
            'node_id': node_id
        }
        
        resp = requests.request('POST', f'http://{self.server_ip}:{self.server_port}/put_one_troop', headers={'x-access-token': self.token}, data=body)
        return self.handel_output(resp)
    
    def put_troop(self, node_id, num):
        body = {
            'node_id': node_id,
            'number_of_troops': num
        }

        resp = requests.request('POST', f'http://{self.server_ip}:{self.server_port}/put_troop', headers={'x-access-token': self.token}, data=body)
        return self.handel_output(resp)

    def get_player_id(self):
        try:
            resp = requests.request('GET', f'http://{self.server_ip}:{self.server_port}/get_player_id', headers={'x-access-token': self.token})
        except:
            print("can't make request")
            return
        return self.handel_output(resp)
    
    def attack(self, attacking_id, target_id, fraction, move_fraction):
        body = {
            'attacking_id': attacking_id,
            'target_id': target_id,
            'fraction': fraction,
            'move_fraction': move_fraction
        }

        resp = requests.request('POST', f'http://{self.server_ip}:{self.server_port}/attack', headers={'x-access-token': self.token}, data=body)
        return self.handel_output(resp)
    
    def move_troop(self, source, destination, troop_count):
        body = {
            'source': source,
            'destination': destination,
            'troop_count': troop_count
        }

        resp = requests.request('POST', f'http://{self.server_ip}:{self.server_port}/move_troop', headers={'x-access-token': self.token}, data=body)
        return self.handel_output(resp)
    
    def get_strategic_nodes(self):
        try:
            resp = requests.request('GET', f'http://{self.server_ip}:{self.server_port}/get_strategic_nodes', headers={'x-access-token': self.token})
        except:
            print("can't make request")
            return
        return self.handel_output(resp)
    
    def get_number_of_troops_to_put(self):
        try:
            resp = requests.request('GET', f'http://{self.server_ip}:{self.server_port}/get_number_of_troops_to_put', headers={'x-access-token': self.token})
        except:
            print("can't make request")
            return
        return self.handel_output(resp)
    
    def get_reachable(self, node_id):
        body = {
            'node_id': node_id
        }

        resp = requests.request('POST', f'http://{self.server_ip}:{self.server_port}/get_reachable', headers={'x-access-token': self.token}, data=body)
        return self.handel_output(resp)