# _*_ coding: utf-8 _*_
import json
import threading
import time
import urllib.request

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QFrame, QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from src.UDP_Socket import NetworkManager
from ui.mainwindow_design import Ui_MainWindow


class CameraStreamWorker(threading.Thread):

    _stop = False
    _label = None
    _url = ''

    def __init__(self, qlabel, url):
        threading.Thread.__init__(self)
        self._label = qlabel
        self._url = url

    def run(self):

        while True:
            try:
                if self._stop == False:
                    data = urllib.request.urlopen(self._url).read()
                    pixmap = QPixmap()
                    pixmap.loadFromData(data)
                    self._label.setPixmap(pixmap)

                    time.sleep(0.2)
            except Exception as e:
                print(e)



class MainWindow(QMainWindow, Ui_MainWindow):
    html_src = '<html>\n<body>\n<img src="http://172.16.255.1:8080/?action=stream" width="640" height="480">\n</body>\n</html>'

    pressedTime = 0

    stream_worker = None
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.init_ui()

    def keyPressEvent(self, event):
        nowtime = int(round(time.time() * 1000))

        if nowtime - self.pressedTime > 100:
            self.pressedTime = nowtime

            press_key = chr(event.key())
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

    def movecar(self, direction):

        try:
            datas = []

            datas.append(direction)
            dict_data = {}
            dict_data['header'] = NetworkManager.HEADER
            dict_data['protocol'] = 'move'
            dict_data['datas'] = datas

            json_val = json.dumps(dict_data)
            NetworkManager.send_data(json_val)
        except Exception as e:
            print(e)

    def init_ui(self):
        try:
            self.stream_worker = CameraStreamWorker(self.lbl_camerea, 'http://172.16.255.1:8080/?action=snapshot')
            self.stream_worker.start()

        except Exception as e:
            print(e)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.resize(myWindow.width(), myWindow.height())
    myWindow.show()
    app.exec_()
