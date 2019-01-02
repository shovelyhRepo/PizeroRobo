from src.functions.func_drive import DriveManager, DRIVE_COMMAND
from src.functions.func_gpio import GPIO_Manager
from src.functions.func_gpio import PIN_DEF
from src.functions.func_network import NetworkManager
import time




class MainApp:
    arrCmd = []
    ctr_idx = 0

    def __init__(self):
        pass
        #for i in range(5):
        #    self.arrCmd.append(DRIVE_COMMAND.CMD_STOP + i)

    def excute_app(self):
        NetworkManager.run()
        '''
         while True:
            DriveManager.command_drive(self.arrCmd[self.ctr_idx])
            time.sleep(1)
            self.ctr_idx = self.ctr_idx + 1

            if self.ctr_idx >= len(self.arrCmd):
                self.ctr_idx = 0
        '''