import json

from src.UDP_Socket import NetworkManager


class UDP_Protocols:
    HEADER = 'RPZero_RobotCar_Control,1.0'
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
        pass

    def movecar(self, direction):
        try:
            datas = []

            datas.append(direction)
            dict_data = {}
            dict_data['header'] = UDP_Protocols.HEADER
            dict_data['protocol'] = 'move'
            dict_data['datas'] = datas

            json_val = json.dumps(dict_data)
            NetworkManager.send_data(json_val)
        except Exception as e:
            print(e)

ProcotcolManager = UDP_Protocols.instance()