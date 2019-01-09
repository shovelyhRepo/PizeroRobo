import os, sys, platform

from ui.mainwindow import Main_Window
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication
from ui.mainwindow_worker import Main_Window_Worker

if __name__ == "__main__":


    app = QApplication(sys.argv)

    myWindow = Main_Window(Main_Window_Worker)
    myWindow.resize(myWindow.width(), myWindow.height())
    if platform.system() == "Windows":
        QApplication.setOverrideCursor(QCursor(QtCore.Qt.ArrowCursor))
        myWindow.show()
    else:
        # full screen
        QApplication.setOverrideCursor(QCursor(QtCore.Qt.BlankCursor))
        myWindow.showFullScreen()
    app.exec_()