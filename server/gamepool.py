
import json
import time
from enums import RequestStatus
from client import Client

class GamePool:

    def __init__(self):
        self.lobbys = []
        self.clients = []

    def client_request(self, address, request):

        data = None
        try:
            data = json.loads(request)
        except json.JSONDecodeError:
            print(f"invalid json: {address} ")
            return (RequestStatus.SOFTERROR, '{"status": "invalid request: could not parse json data"}')

        # process requests

        # check if type is here
        if "type" not in data:
            print(f"no request type: {address} ")
            return (RequestStatus.SOFTERROR, '{"status": "invalid request: no request type qiven"}')

        try:
            return self.request_functions[data["type"]](self, address, request)
        except KeyError:
            print(f"invalid request type: {address} ")
            return (RequestStatus.SOFTERROR, '{"status": "invalid request: wrong request type given"}')

    def client_disconnected(self, address):
        client = self.find_client(address)
        if client != None:
            self.clients.remove(client)
        print(f"disconnect: {address} - currently connected {len(self.clients)}")
    
    def find_client(self, address):
        for x in self.clients:
            if x.ip == address[0] and x.port == address[1]:
                return x
        return None

    def find_lobby(self, id):
        pass

    def request_join(self, address, request):

        client = self.find_client(address)
        if client != None:
            print(f"weird rejoin: {address} ")
            return (RequestStatus.SOFTERROR, '{"status": "rejoined, but was not disconnected"}')

        else:
            new_client = Client(address)
            self.clients.append(new_client)
            print(f"join: {address} - currently connected {len(self.clients)}")
            return (RequestStatus.OK, '{"status": "connected!"}')

    def request_create_lobby(self, address, request):
        pass

    request_functions = {

        "join": request_join,
        "mklobby": request_create_lobby

    }