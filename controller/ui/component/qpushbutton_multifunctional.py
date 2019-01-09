from PyQt5.QtCore import pyqtSignal, QSize
from PyQt5.QtWidgets import QPushButton



class QPushButtonMultiFunctional(QPushButton):
    doubleClicked = pyqtSignal()
    icons = None
    btnObj = None

    def __init__(self, parent=None):
        super().__init__(parent)
        self.obj = None

    def object(self):
        return self.obj

    def setObject(self, obj):
        self.obj = obj

    def hasObject(self):
        return bool(self.obj)

    def setIconResource(self, icons):
        self.icons = icons

    def hitButton(self, *args, **kwargs):
        if self.isDown():
            pass
        return True

    def mouseDoubleClickEvent(self, *args, **kwargs):
        self.doubleClicked.emit()
