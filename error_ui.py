# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ErrorWin(object):
    def setupUi(self, ErrorWin):
        ErrorWin.setObjectName("ErrorWin")
        ErrorWin.resize(408, 294)
        self.label = QtWidgets.QLabel(ErrorWin)
        self.label.setGeometry(QtCore.QRect(20, 0, 81, 71))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(ErrorWin)
        self.pushButton.setGeometry(QtCore.QRect(150, 230, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.error_info = QtWidgets.QTextBrowser(ErrorWin)
        self.error_info.setGeometry(QtCore.QRect(20, 60, 341, 161))
        self.error_info.setObjectName("error_info")

        self.retranslateUi(ErrorWin)
        self.pushButton.clicked.connect(ErrorWin.close)
        QtCore.QMetaObject.connectSlotsByName(ErrorWin)

    def retranslateUi(self, ErrorWin):
        _translate = QtCore.QCoreApplication.translate
        ErrorWin.setWindowTitle(_translate("ErrorWin", "Dialog"))
        self.label.setText(_translate("ErrorWin", "ERROR!"))
        self.pushButton.setText(_translate("ErrorWin", "OK"))
        self.pushButton.setShortcut(_translate("ErrorWin", "Space"))