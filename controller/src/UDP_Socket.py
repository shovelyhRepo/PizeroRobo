import threading, time
import socket
import json, sys

class UDP_Socket:
    HEADER = 'RPZero_RobotCar_Control,1.0'
    _socket = None
    __port = 0
    server_address = '172.16.255.1'
    #server_address = '127.0.0.1'

    __instance = None

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance

    def __init__(self):
        self.__port = 12000
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #self._socket.bind(('', self.__port))

    def send_data(self, data):
        self._socket.sendto(data.encode('utf-8'), (self.server_address, self.__port))
def movecar(socket, direction):
    datas = []

    datas.append(direction)
    dict_data = {}
    dict_data['header'] = UDP_Socket.HEADER
    dict_data['protocol'] = 'move'
    dict_data['datas'] = datas

    json_val = json.dumps(dict_data)
    socket.send_data(json_val)

NetworkManager = UDP_Socket.instance()