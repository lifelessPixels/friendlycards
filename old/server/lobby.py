
import hashlib

class Lobby:

    def __init__(self, name, owner, maxplayers=8):
        self.players = [owner]
        self.id = hashlib.md5(name)