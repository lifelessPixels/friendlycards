
from enum import Enum

class ConnectionState(Enum):
    CONNECTED = 0
    DISCONNECTED = 1

class RequestStatus(Enum):
    OK = 0
    SOFTERROR = 1
    HARDERROR = 2