import platform
from enum import IntEnum

class PIN_DEF(IntEnum):
    PIN_LEFT_WHEEL_P = 0
    PIN_LEFT_WHEEL_N = 1
    PIN_RIGHT_WHEEL_P = 2
    PIN_RIGHT_WHEEL_N = 3

if platform.system() != 'Windows':
    import wiringpi

class Func_GPIO:
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
        try:
            wiringpi.wiringPiSetup()
            wiringpi.pinMode(PIN_DEF.PIN_LEFT_WHEEL_P, 1)
            wiringpi.pinMode(PIN_DEF.PIN_RIGHT_WHEEL_P, 1)
            wiringpi.pinMode(PIN_DEF.PIN_LEFT_WHEEL_N, 1)
            wiringpi.pinMode(PIN_DEF.PIN_RIGHT_WHEEL_N, 1)
        except:
            pass

    def writePin(self, pin, signal):
        try:
            if signal == 0:
                signal = 0
            else:
                signal = 1
            wiringpi.digitalWrite(pin, signal)
        except:
            pass


GPIO_Manager = Func_GPIO.instance()