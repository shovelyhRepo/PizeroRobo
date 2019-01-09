# _*_ coding: utf-8 _*_
import threading
import time
import urllib.request

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QFrame, QApplication
from src.Command_Worker import CommandManager
from src.Defines.Command_Type import Command_Type
from src.UDP_Protocols import ProcotcolManager
from ui.main_config import Main_Config
from ui.mainwindow_design import Ui_MainWindow

class CameraStreamWorker(threading.Thread):

    _stop = False
    _label = None
    _url = ''
    exitStream = False

    def __init__(self, qlabel, url):
        threading.Thread.__init__(self)
        self._label = qlabel
        self._url = url

    def run(self):

        while self.exitStream == False:
            try:
                if self._stop == False:
                    data = urllib.request.urlopen(self._url).read()
                    pixmap = QPixmap()
                    pixmap.loadFromData(data)
                    self._label.setPixmap(pixmap)

                    time.sleep(0.1)
            except Exception as e:
                print(e)



class Main_Window(QMainWindow, Ui_MainWindow):
    pressedTime = 0
    stream_worker = None
    mainwindow_worker = None
    btn_icon_resource = [
        (":/png/res/ui/btn_ctrl_up.png", ":/png/res/ui/btn_ctrl_up_1.png"),
        (":/png/res/ui/btn_ctrl_down.png", ":/png/res/ui/btn_ctrl_down_1.png"),
        (":/png/res/ui/btn_ctrl_left.png", ":/png/res/ui/btn_ctrl_left_1.png"),
        (":/png/res/ui/btn_ctrl_right.png", ":/png/res/ui/btn_ctrl_right_1.png"),
    ]

    def __init__(self, worker_cls):
        QMainWindow.__init__(self)

        self.setupUi(self)
        self.init_ui()
        self.init_event()

        CommandManager.init(self)
        CommandManager.start_worker()
        self.mainwindow_worker = worker_cls(self)

    def __del__(self):
        self.stream_worker.exitStream = True

    def update_icon(self, btnobj, icons):
        try:

            #'''
            idle_icon, press_icon = icons

            if btnobj.isChecked() is True:
                print('111111111111111111')
                #self.btnObj.setIcon(QIcon(press_icon))
                #self.btnObj.setStyleSheet('background:url(:{});'.format(press_icon))
            else:
                print('2222222222222222222')
                #self.btnObj.setIcon(QIcon(idle_icon))
                #self.btnObj.setStyleSheet('background:url(:{});'.format(idle_icon))
            #'''
        except Exception as e:
            print(e)

    def init_event(self):
        self.btn_ctrl_up.pressed.connect(self.on_clicked_ctrl_up_pressed)
        self.btn_ctrl_up.clicked.connect(self.on_clicked_ctrl_up_released)
        self.btn_ctrl_down.pressed.connect(self.on_clicked_ctrl_down_pressed)
        self.btn_ctrl_down.clicked.connect(self.on_clicked_ctrl_down_released)
        self.btn_ctrl_left.pressed.connect(self.on_clicked_ctrl_left_pressed)
        self.btn_ctrl_left.clicked.connect(self.on_clicked_ctrl_left_released)
        self.btn_ctrl_right.pressed.connect(self.on_clicked_ctrl_right_pressed)
        self.btn_ctrl_right.clicked.connect(self.on_clicked_ctrl_right_released)

        self.btn_stop.pressed.connect(self.on_clicked_stop_pressed)
        self.btn_stop.clicked.connect(self.on_clicked_stop_released)
        self.btn_shot.pressed.connect(self.on_clicked_capture_pressed)
        self.btn_shot.clicked.connect(self.on_clicked_capture_released)
        self.btn_config.pressed.connect(self.on_clicked_config_pressed)
        self.btn_config.clicked.connect(self.on_clicked_config_released)


    def on_clicked_stop_pressed(self):
        self.btn_stop.setChecked(True)

    def on_clicked_stop_released(self):
        self.btn_stop.setChecked(False)
        ProcotcolManager.movecar('stop')

    def on_clicked_capture_pressed(self):
        self.btn_shot.setChecked(True)

    def on_clicked_capture_released(self):
        self.btn_shot.setChecked(False)

    def on_clicked_config_pressed(self):
        self.btn_config.setChecked(True)

    def on_clicked_config_released(self):
        self.btn_config.setChecked(False)
        CommandManager.put_command(Command_Type.CMD_OPEN_UI)



    def on_clicked_ctrl_up_pressed(self):
        self.btn_ctrl_up.setChecked(True)

    def on_clicked_ctrl_up_released(self):
        self.btn_ctrl_up.setChecked(False)
        ProcotcolManager.movecar('front')

    def on_clicked_ctrl_down_pressed(self):
        self.btn_ctrl_down.setChecked(True)

    def on_clicked_ctrl_down_released(self):
        self.btn_ctrl_down.setChecked(False)
        ProcotcolManager.movecar('back')

    def on_clicked_ctrl_left_pressed(self):
        self.btn_ctrl_left.setChecked(True)

    def on_clicked_ctrl_left_released(self):
        self.btn_ctrl_left.setChecked(False)
        ProcotcolManager.movecar('left')

    def on_clicked_ctrl_right_pressed(self):
        self.btn_ctrl_right.setChecked(True)

    def on_clicked_ctrl_right_released(self):
        self.btn_ctrl_right.setChecked(False)
        ProcotcolManager.movecar('right')

    def keyPressEvent(self, event):
        nowtime = int(round(time.time() * 1000))

        if nowtime - self.pressedTime > 100:
            self.pressedTime = nowtime

            press_key = chr(event.key())
            '''
            if press_key == 'W':
                self.movecar('front')
            elif press_key == 'S':
                self.movecar('back')
            elif press_key == 'A':
                self.movecar('left')
            elif press_key == 'D':
                self.movecar('right')
            elif press_key == 'Z':
                self.movecar('stop')
            elif press_key == 'Q':
                sys.exit()
            '''


    def init_ui(self):

        self.ui_config =  Main_Config(self.content_frame)
        self.ui_config.hide()

        self.content_frame.hide()
        try:
            self.stream_worker = CameraStreamWorker(self.lbl_camerea, 'http://172.16.255.1:8080/?action=snapshot')
            self.stream_worker.start()

            #icon = QIcon()
            #icon.addPixmap(QPixmap(self.btn_icon_resource[0][0]))
            #icon.addPixmap(QPixmap(self.btn_icon_resource[0][1]), QIcon.Active)
            #self.btn_ctrl_up.setIcon(icon)

        except Exception as e:
            print(e)

