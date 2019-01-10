import os, sys, platform

from ui.main_config_worker import Main_Config_Worker
from ui.mainwindow import Main_Window
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication
from ui.mainwindow_worker import Main_Window_Worker

if __name__ == "__main__":

    app = QApplication(sys.argv)

    myWindow = Main_Window()
    myWindow.resize(800, 480)

    #add worker
    myWindow.add_worker(Main_Window_Worker)
    myWindow.add_worker(Main_Config_Worker)

    if platform.system() == "Windows":
        QApplication.setOverrideCursor(QCursor(QtCore.Qt.ArrowCursor))
        myWindow.show()
    else:
        # full screen
        QApplication.setOverrideCursor(QCursor(QtCore.Qt.BlankCursor))
        myWindow.showFullScreen()
    app.exec_()