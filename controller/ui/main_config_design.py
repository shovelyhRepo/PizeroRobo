# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\..\ui\main_config.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Main_Config(object):
    def setupUi(self, Main_Config):
        Main_Config.setObjectName("Main_Config")
        Main_Config.resize(800, 480)
        Main_Config.setStyleSheet("background:rgba(60, 60, 60, 200);")
        self.frame_config = QtWidgets.QFrame(Main_Config)
        self.frame_config.setGeometry(QtCore.QRect(100, 16, 600, 450))
        self.frame_config.setStyleSheet("background:rgba(40, 40, 40, 200);")
        self.frame_config.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_config.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_config.setObjectName("frame_config")
        self.lbl_popup_uptitle = QtWidgets.QLabel(self.frame_config)
        self.lbl_popup_uptitle.setGeometry(QtCore.QRect(0, 0, 640, 50))
        font = QtGui.QFont()
        font.setFamily("NanumBarunGothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_popup_uptitle.setFont(font)
        self.lbl_popup_uptitle.setStyleSheet("background:rgba(180, 200, 220, 200);\n"
"")
        self.lbl_popup_uptitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_popup_uptitle.setObjectName("lbl_popup_uptitle")
        self.btn_popup_close = QtWidgets.QPushButton(self.frame_config)
        self.btn_popup_close.setGeometry(QtCore.QRect(550, 0, 50, 50))
        font = QtGui.QFont()
        font.setFamily("NanumBarunGothic")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.btn_popup_close.setFont(font)
        self.btn_popup_close.setStyleSheet("QWidget::enabled{\n"
"    background:rgba(200, 0, 0, 200);\n"
"    border-style:outer;\n"
"}\n"
"QWidget::checked{\n"
"\n"
"    background:rgba(255, 108, 110, 200);\n"
"    border-style:outer;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"   color:white;\n"
"}\n"
"")
        self.btn_popup_close.setObjectName("btn_popup_close")
        self.widget_config_robotip = QtWidgets.QWidget(self.frame_config)
        self.widget_config_robotip.setGeometry(QtCore.QRect(15, 80, 571, 80))
        self.widget_config_robotip.setObjectName("widget_config_robotip")
        self.widget_config_robot_ms = QtWidgets.QWidget(self.frame_config)
        self.widget_config_robot_ms.setGeometry(QtCore.QRect(15, 180, 571, 80))
        self.widget_config_robot_ms.setObjectName("widget_config_robot_ms")

        self.retranslateUi(Main_Config)
        QtCore.QMetaObject.connectSlotsByName(Main_Config)

    def retranslateUi(self, Main_Config):
        _translate = QtCore.QCoreApplication.translate
        Main_Config.setWindowTitle(_translate("Main_Config", "Form"))
        self.lbl_popup_uptitle.setText(_translate("Main_Config", "Config"))
        self.btn_popup_close.setText(_translate("Main_Config", "X"))

