import threading, time
import socket
import json

from src.functions.func_drive import DriveManager,DRIVE_COMMAND


class UDP_RecvWorker(threading.Thread):

    PORT = 0
    exitThd = False
    _socket = None
    def __init__(self):
        threading.Thread.__init__(self)
        self.PORT = 12000
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __del__(self):
        self.exitThd = True

    def run(self):
        try:
            self._socket.bind(('', self.PORT))
            while self.exitThd == False:
                data, ip_addr = self._socket.recvfrom(2048)
                #print('[{}] data = {}'.format(ip_addr, data.decode('utf-8')))
                NetworkManager.addwork(data, ip_addr)
                time.sleep(0.1)
        except Exception as e:
            print(e)

class Func_Network:
    __instance = None
    work_list = []
    listener_list = []
    THREAD_COUNT = 1
    HEADER = 'RPZero_RobotCar_Control,1.0'

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance

    def addwork(self, data, ip_addr):
        self.work_list.append((data.decode('utf-8'), ip_addr))

    def dowork(self, workdata):

        try:
            data = workdata[0]
            ip_addr_port = workdata[1]
            print('[{}] data = {}'.format(ip_addr_port, data))

            dict_data = json.loads(data)
            header = dict_data['header']
            protocol = dict_data['protocol']
            datas = dict_data['datas']

            if header == self.HEADER:
                if protocol == 'move':
                    direction = datas[0]

                    if direction == 'stop':
                        DriveManager.command_drive(DRIVE_COMMAND.CMD_STOP)
                    elif direction == 'left':
                        DriveManager.command_drive(DRIVE_COMMAND.CMD_TURN_LEFT)
                    elif direction == 'right':
                        DriveManager.command_drive(DRIVE_COMMAND.CMD_TURN_RIGHT)
                    elif direction == 'front':
                        DriveManager.command_drive(DRIVE_COMMAND.CMD_FRONT)
                    elif direction == 'back':
                        DriveManager.command_drive(DRIVE_COMMAND.CMD_BACK)

        except Exception as e:
            print(e)

    def __init__(self):
        self.PORT = 12000
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        for i in range(self.THREAD_COUNT):
            th = UDP_RecvWorker()
            self.listener_list.append(th)
            th.start()
            print('[{}] start udp listen'.format(i))

    def run(self):
        while True:
            try:
                for work in self.work_list:
                    self.dowork(work)
                    self.work_list.remove(work)
            except Exception as e:
                print(e)

NetworkManager = Func_Network.instance()