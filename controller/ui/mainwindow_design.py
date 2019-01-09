# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\..\ui\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_camerea = QtWidgets.QLabel(self.centralwidget)
        self.lbl_camerea.setGeometry(QtCore.QRect(250, 10, 320, 240))
        self.lbl_camerea.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_camerea.setText("")
        self.lbl_camerea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lbl_camerea.setObjectName("lbl_camerea")
        self.btn_ctrl_left = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ctrl_left.setGeometry(QtCore.QRect(30, 280, 96, 74))
        self.btn_ctrl_left.setStyleSheet("\n"
"QWidget::enabled{\n"
"    background:url(:/png/res/ui/btn_ctrl_left.png);\n"
"\n"
"    border-style:outer;\n"
"}\n"
"QWidget::checked{\n"
"    background:url(:/png/res/ui/btn_ctrl_left_1.png);\n"
"    border-style:outer;\n"
"}\n"
"")
        self.btn_ctrl_left.setText("")
        self.btn_ctrl_left.setCheckable(True)
        self.btn_ctrl_left.setObjectName("btn_ctrl_left")
        self.btn_ctrl_right = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ctrl_right.setGeometry(QtCore.QRect(190, 280, 96, 74))
        self.btn_ctrl_right.setStyleSheet("\n"
"QWidget::enabled{\n"
"    background:url(:/png/res/ui/btn_ctrl_right.png);\n"
"\n"
"    border-style:outer;\n"
"}\n"
"QWidget::checked{\n"
"    background:url(:/png/res/ui/btn_ctrl_right_1.png);\n"
"    border-style:outer;\n"
"}\n"
"")
        self.btn_ctrl_right.setText("")
        self.btn_ctrl_right.setCheckable(True)
        self.btn_ctrl_right.setObjectName("btn_ctrl_right")
        self.btn_ctrl_down = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ctrl_down.setGeometry(QtCore.QRect(120, 350, 74, 96))
        self.btn_ctrl_down.setStyleSheet("\n"
"QWidget::enabled{\n"
"    background:url(:/png/res/ui/btn_ctrl_down.png);\n"
"\n"
"    border-style:outer;\n"
"}\n"
"QWidget::checked{\n"
"    background:url(:/png/res/ui/btn_ctrl_down_1.png);\n"
"    border-style:outer;\n"
"}\n"
"")
        self.btn_ctrl_down.setText("")
        self.btn_ctrl_down.setCheckable(True)
        self.btn_ctrl_down.setObjectName("btn_ctrl_down")
        self.lbl_bg = QtWidgets.QLabel(self.centralwidget)
        self.lbl_bg.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.lbl_bg.setStyleSheet("background-image: url(:/png/res/ui/bg_1.png);\n"
"background-position:center;\n"
"background-repeat:norepeat;\n"
"")
        self.lbl_bg.setText("")
        self.lbl_bg.setObjectName("lbl_bg")
        self.btn_ctrl_up = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ctrl_up.setGeometry(QtCore.QRect(120, 190, 74, 96))
        self.btn_ctrl_up.setStyleSheet("QWidget::enabled{\n"
"    background:url(:/png/res/ui/btn_ctrl_up.png);\n"
"\n"
"    border-style:outer;\n"
"}\n"
"QWidget::checked{\n"
"    background:url(:/png/res/ui/btn_ctrl_up_1.png);\n"
"    border-style:outer;\n"
"}\n"
"")
        self.btn_ctrl_up.setText("")
        self.btn_ctrl_up.setCheckable(True)
        self.btn_ctrl_up.setChecked(False)
        self.btn_ctrl_up.setAutoRepeat(False)
        self.btn_ctrl_up.setAutoExclusive(False)
        self.btn_ctrl_up.setObjectName("btn_ctrl_up")
        self.btn_config = QtWidgets.QPushButton(self.centralwidget)
        self.btn_config.setGeometry(QtCore.QRect(700, 20, 74, 71))
        font = QtGui.QFont()
        font.setFamily("NanumBarunGothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_config.setFont(font)
        self.btn_config.setStyleSheet("QWidget::enabled{\n"
"    background:url(:/png/res/ui/btn_idle.png);\n"
"    border-style:outer;\n"
"}\n"
"QWidget::checked{\n"
"    background:url(:/png/res/ui/btn_press.png);\n"
"    border-style:outer;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"   color:white;\n"
"}\n"
"\n"
"\n"
"")
        self.btn_config.setCheckable(True)
        self.btn_config.setObjectName("btn_config")
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setGeometry(QtCore.QRect(430, 380, 75, 75))
        font = QtGui.QFont()
        font.setFamily("NanumBarunGothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_stop.setFont(font)
        self.btn_stop.setStyleSheet("QWidget::enabled{\n"
"    background:url(:/png/res/ui/btn_idle.png);\n"
"    border-style:outer;\n"
"}\n"
"QWidget::checked{\n"
"    background:url(:/png/res/ui/btn_press.png);\n"
"    border-style:outer;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"   color:white;\n"
"}\n"
"\n"
"\n"
"")
        self.btn_stop.setCheckable(True)
        self.btn_stop.setObjectName("btn_stop")
        self.btn_shot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_shot.setGeometry(QtCore.QRect(620, 380, 75, 75))
        font = QtGui.QFont()
        font.setFamily("NanumBarunGothic")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_shot.setFont(font)
        self.btn_shot.setStyleSheet("QWidget::enabled{\n"
"    background:url(:/png/res/ui/btn_idle.png);\n"
"    border-style:outer;\n"
"}\n"
"QWidget::checked{\n"
"    background:url(:/png/res/ui/btn_press.png);\n"
"    border-style:outer;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"   color:white;\n"
"}\n"
"\n"
"\n"
"")
        self.btn_shot.setCheckable(True)
        self.btn_shot.setObjectName("btn_shot")
        self.content_frame = QtWidgets.QFrame(self.centralwidget)
        self.content_frame.setEnabled(True)
        self.content_frame.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.content_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_frame.setObjectName("content_frame")
        self.lbl_bg.raise_()
        self.btn_ctrl_left.raise_()
        self.btn_ctrl_down.raise_()
        self.btn_ctrl_right.raise_()
        self.lbl_camerea.raise_()
        self.btn_ctrl_up.raise_()
        self.btn_config.raise_()
        self.btn_stop.raise_()
        self.btn_shot.raise_()
        self.content_frame.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_config.setText(_translate("MainWindow", "Config"))
        self.btn_stop.setText(_translate("MainWindow", "Stop"))
        self.btn_shot.setText(_translate("MainWindow", "Shot"))

import resource_rc
