# _*_ coding: utf-8 _*_

from PyQt5.QtWidgets import QFrame
from ui.main_config_design import Ui_Main_Config



class Main_Config(QFrame, Ui_Main_Config):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.init_ui()
        self.init_event()

    def init_event(self):
        self.btn_popup_close.pressed.connect(self.on_click_close_pressed)
        self.btn_popup_close.released.connect(self.on_click_close_released)

    def init_ui(self):
        pass

    def on_click_close_pressed(self):
        self.btn_popup_close.setChecked(True)

    def on_click_close_released(self):

        try:
            self.btn_popup_close.setChecked(False)

            if self.isVisible() == True:
                self.setVisible(False)
        except Exception as e:
            print(e)