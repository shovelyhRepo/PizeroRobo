# _*_ coding: utf-8 _*_
import os
import platform
import sys
import time

from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication
from ui.


if __name__ == "__main__":

    try:
        app = QApplication(sys.argv)

        CubiLog.info("start Main_Window {0}".format(__file__))
        myWindow = Main_Window(Main_Window_Observer)
        myWindow.resize(myWindow.width(), myWindow.height())
        if platform.system() == "Windows":
            QApplication.setOverrideCursor(QCursor(QtCore.Qt.ArrowCursor))
            myWindow.show()
        else:
            # full screen
            QApplication.setOverrideCursor(QCursor(QtCore.Qt.BlankCursor))
            myWindow.showFullScreen()

        if platform.system() != "Windows":
            #system_util.start_pscheck()
            os.system('sudo pkill -9 -ef version_selector.py')
            #time.sleep(0.1)
            system_util.update_autostart()
        app.exec_()
        CubiLog.info("end Main_Window {0}".format(__file__))
        os.system("~/CubiMaker/shell/killCubimaker.sh")
        app.exit()
    except Exception as e:
        CubiLog.exception(e)
