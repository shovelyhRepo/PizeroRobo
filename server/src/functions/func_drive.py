import threading
import time
from enum import IntEnum

from src.functions.func_gpio import GPIO_Manager, PIN_DEF


class DRIVE_COMMAND(IntEnum):
    CMD_STOP = 0
    CMD_TURN_LEFT = 1
    CMD_TURN_RIGHT = 2
    CMD_FRONT = 3
    CMD_BACK = 4

class DriveWorker(threading.Thread):
    exitThd = False
    exe_starttime = 0
    exe_cmd = DRIVE_COMMAND.CMD_STOP
    exe_keeptime = 0

    def __init__(self):
        threading.Thread.__init__(self)

    def __del__(self):
        self.exitThd = True

    def excute_drive(self, cmd=DRIVE_COMMAND.CMD_STOP, time_ms=300):
        self.exe_cmd = cmd
        self.exe_keeptime = time_ms
        self.exe_starttime = int(round(time.time() * 1000))

    def go_left(self):
        GPIO_Manager.writePin(PIN_DEF.PIN_LEFT_WHEEL_P, 1)
        GPIO_Manager.writePin(PIN_DEF.PIN_LEFT_WHEEL_N, 0)
        GPIO_Manager.writePin(PIN_DEF.PIN_RIGHT_WHEEL_P, 0)
        GPIO_Manager.writePin(PIN_DEF.PIN_RIGHT_WHEEL_N, 1)

    def go_right(self):
        GPIO_Manager.writePin(PIN_DEF.PIN_LEFT_WHEEL_P, 0)
        GPIO_Manager.writePin(PIN_DEF.PIN_LEFT_WHEEL_N, 1)
        GPIO_Manager.writePin(PIN_DEF.PIN_RIGHT_WHEEL_P, 1)
        GPIO_Manager.writePin(PIN_DEF.PIN_RIGHT_WHEEL_N, 0)

    def go_front(self):
        GPIO_Manager.writePin(PIN_DEF.PIN_LEFT_WHEEL_P, 1)
        GPIO_Manager.writePin(PIN_DEF.PIN_LEFT_WHEEL_N, 0)
        GPIO_Manager.writePin(PIN_DEF.PIN_RIGHT_WHEEL_P, 1)
        GPIO_Manager.writePin(PIN_DEF.PIN_RIGHT_WHEEL_N, 0)

    def go_back(self):
        GPIO_Manager.writePin(PIN_DEF.PIN_LEFT_WHEEL_P, 0)
        GPIO_Manager.writePin(PIN_DEF.PIN_LEFT_WHEEL_N, 1)
        GPIO_Manager.writePin(PIN_DEF.PIN_RIGHT_WHEEL_P, 0)
        GPIO_Manager.writePin(PIN_DEF.PIN_RIGHT_WHEEL_N, 1)

    def stop_drive(self):
        GPIO_Manager.writePin(PIN_DEF.PIN_LEFT_WHEEL_P, 0)
        GPIO_Manager.writePin(PIN_DEF.PIN_LEFT_WHEEL_N, 0)
        GPIO_Manager.writePin(PIN_DEF.PIN_RIGHT_WHEEL_P, 0)
        GPIO_Manager.writePin(PIN_DEF.PIN_RIGHT_WHEEL_N, 0)

    def run(self):
        while self.exitThd == False:
            nowtime = int(round(time.time() * 1000))

            if nowtime - self.exe_starttime < self.exe_keeptime:
                if self.exe_cmd == DRIVE_COMMAND.CMD_STOP:
                    #print('ms : {} cmd : {}'.format(nowtime - self.exe_starttime, self.exe_cmd))
                    self.stop_drive()
                elif self.exe_cmd == DRIVE_COMMAND.CMD_TURN_LEFT:
                    #print('ms : {} cmd : {}'.format(nowtime - self.exe_starttime, self.exe_cmd))
                    self.go_left()
                elif self.exe_cmd == DRIVE_COMMAND.CMD_TURN_RIGHT:
                    #print('ms : {} cmd : {}'.format(nowtime - self.exe_starttime, self.exe_cmd))
                    self.go_right()
                elif self.exe_cmd == DRIVE_COMMAND.CMD_FRONT:
                    #print('ms : {} cmd : {}'.format(nowtime - self.exe_starttime, self.exe_cmd))
                    self.go_front()
                elif self.exe_cmd == DRIVE_COMMAND.CMD_BACK:
                    #print('ms : {} cmd : {}'.format(nowtime - self.exe_starttime, self.exe_cmd))
                    self.go_back()
            else:
                self.stop_drive()

class Func_Drive:

    __instance = None
    drive_thread = None

    @classmethod
    def __getInstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kargs):
        cls.__instance = cls(*args, **kargs)
        cls.instance = cls.__getInstance
        return cls.__instance

    def __init__(self):
        self.drive_thread = DriveWorker()
        self.drive_thread.start()

    def command_drive(self, cmd):
        self.drive_thread.excute_drive(cmd, 150)


DriveManager = Func_Drive.instance()