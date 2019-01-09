import threading, time
import socket
import json, sys

class UDP_Socket:
    _socket = None
    __port = 0
    server_address = '172.16.255.1'
    #server_address = '192.168.0.108'

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

NetworkManager = UDP_Socket.instance()