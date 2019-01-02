import threading, time
import socket
import json
import pygame, sys
import pygame.locals



HEADER = 'RPZero_RobotCar_Control,1.0'
class UDP_Socket:
    _socket = None
    __port = 0
    server_address = '172.16.255.1'
    #server_address = '127.0.0.1'

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
    dict_data['header'] = HEADER
    dict_data['protocol'] = 'move'
    dict_data['datas'] = datas

    json_val = json.dumps(dict_data)
    socket.send_data(json_val)





if __name__ == '__main__':
    obj = UDP_Socket()
    pygame.init()
    BLACK = (0, 0, 0)
    WIDTH = 640
    HEIGHT = 480
    windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

    windowSurface.fill(BLACK)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == 119: # w
                    movecar(obj, 'front')
                elif event.key == 115: # s
                    movecar(obj, 'back')
                elif event.key == 97: # a
                    movecar(obj, 'left')
                elif event.key == 100: # d
                    movecar(obj, 'right')
                elif event.key == 122: # z
                    movecar(obj, 'stop')
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
