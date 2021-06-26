# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Student_Interface(object):
    def setupUi(self, Student_Interface):
        Student_Interface.setObjectName("Student_Interface")
        Student_Interface.resize(1016, 980)
        Student_Interface.setStyleSheet("background-image: url(:/background/ui_source/water3.png);")
        self.label = QtWidgets.QLabel(Student_Interface)
        self.label.setGeometry(QtCore.QRect(420, 30, 221, 51))
        font = QtGui.QFont()
        font.setFamily("汀明体")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Student_Interface)
        self.tableWidget.setGeometry(QtCore.QRect(50, 240, 941, 361))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setInputMethodHints(QtCore.Qt.ImhNoEditMenu)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.label_5 = QtWidgets.QLabel(Student_Interface)
        self.label_5.setGeometry(QtCore.QRect(70, 611, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.layoutWidget = QtWidgets.QWidget(Student_Interface)
        self.layoutWidget.setGeometry(QtCore.QRect(120, 180, 801, 60))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.state = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.state.setFont(font)
        self.state.setObjectName("state")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.state.addItem("")
        self.horizontalLayout.addWidget(self.state)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.order = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.order.setFont(font)
        self.order.setObjectName("order")
        self.order.addItem("")
        self.order.addItem("")
        self.horizontalLayout_2.addWidget(self.order)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.confirm_disp = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.confirm_disp.setFont(font)
        self.confirm_disp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.confirm_disp.setObjectName("confirm_disp")
        self.gridLayout.addWidget(self.confirm_disp, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(Student_Interface)
        self.label_12.setGeometry(QtCore.QRect(599, 610, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(Student_Interface)
        self.label_14.setGeometry(QtCore.QRect(70, 830, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.layoutWidget1 = QtWidgets.QWidget(Student_Interface)
        self.layoutWidget1.setGeometry(QtCore.QRect(70, 660, 921, 161))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.new_leaving = QtWidgets.QDateTimeEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_leaving.setFont(font)
        self.new_leaving.setDate(QtCore.QDate(2021, 1, 1))
        self.new_leaving.setObjectName("new_leaving")
        self.gridLayout_2.addWidget(self.new_leaving, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.new_return = QtWidgets.QDateTimeEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_return.setFont(font)
        self.new_return.setDate(QtCore.QDate(2021, 1, 1))
        self.new_return.setObjectName("new_return")
        self.gridLayout_2.addWidget(self.new_return, 1, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.new_content = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_content.setFont(font)
        self.new_content.setObjectName("new_content")
        self.gridLayout_2.addWidget(self.new_content, 2, 2, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_2)
        self.new_confirm = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_confirm.setFont(font)
        self.new_confirm.setObjectName("new_confirm")
        self.horizontalLayout_4.addWidget(self.new_confirm)
        spacerItem = QtWidgets.QSpacerItem(128, 136, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.rev_return = QtWidgets.QDateTimeEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rev_return.setFont(font)
        self.rev_return.setDate(QtCore.QDate(2021, 1, 1))
        self.rev_return.setObjectName("rev_return")
        self.gridLayout_3.addWidget(self.rev_return, 2, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 2, 1, 1, 1)
        self.rev_leaving = QtWidgets.QDateTimeEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rev_leaving.setFont(font)
        self.rev_leaving.setDate(QtCore.QDate(2021, 1, 1))
        self.rev_leaving.setObjectName("rev_leaving")
        self.gridLayout_3.addWidget(self.rev_leaving, 1, 3, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 3, 1, 1, 1)
        self.rev_content = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rev_content.setFont(font)
        self.rev_content.setObjectName("rev_content")
        self.gridLayout_3.addWidget(self.rev_content, 3, 3, 1, 1)
        self.rev_app_id = QtWidgets.QLineEdit(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rev_app_id.setFont(font)
        self.rev_app_id.setObjectName("rev_app_id")
        self.gridLayout_3.addWidget(self.rev_app_id, 0, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 0, 1, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout_3)
        self.rev_confirm = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rev_confirm.setFont(font)
        self.rev_confirm.setObjectName("rev_confirm")
        self.horizontalLayout_4.addWidget(self.rev_confirm)
        self.layoutWidget2 = QtWidgets.QWidget(Student_Interface)
        self.layoutWidget2.setGeometry(QtCore.QRect(70, 880, 351, 31))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_3.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_3.addWidget(self.label_16)
        self.cancel_app_id = QtWidgets.QLineEdit(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel_app_id.setFont(font)
        self.cancel_app_id.setObjectName("cancel_app_id")
        self.horizontalLayout_3.addWidget(self.cancel_app_id)
        self.cancel_confirm = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel_confirm.setFont(font)
        self.cancel_confirm.setObjectName("cancel_confirm")
        self.horizontalLayout_3.addWidget(self.cancel_confirm)
        self.self_info = QtWidgets.QTextBrowser(Student_Interface)
        self.self_info.setGeometry(QtCore.QRect(70, 90, 861, 61))
        font = QtGui.QFont()
        font.setFamily("汀明体")
        font.setPointSize(12)
        self.self_info.setFont(font)
        self.self_info.setObjectName("self_info")

        self.retranslateUi(Student_Interface)
        QtCore.QMetaObject.connectSlotsByName(Student_Interface)

    def retranslateUi(self, Student_Interface):
        _translate = QtCore.QCoreApplication.translate
        Student_Interface.setWindowTitle(_translate("Student_Interface", "Form"))
        self.label.setText(_translate("Student_Interface", "学生申请界面"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Student_Interface", "项目"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Student_Interface", "申请编号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Student_Interface", "离开时间"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Student_Interface", "返回时间"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Student_Interface", "审批状态"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Student_Interface", "申请内容"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Student_Interface", "审批回应内容"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Student_Interface", "审批时间"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label_5.setText(_translate("Student_Interface", "新建申请"))
        self.label_3.setText(_translate("Student_Interface", "状态筛选："))
        self.state.setItemText(0, _translate("Student_Interface", "All"))
        self.state.setItemText(1, _translate("Student_Interface", "Pending"))
        self.state.setItemText(2, _translate("Student_Interface", "Passed"))
        self.state.setItemText(3, _translate("Student_Interface", "Refused"))
        self.state.setItemText(4, _translate("Student_Interface", "Cancelled"))
        self.label_2.setText(_translate("Student_Interface", "时间排序："))
        self.order.setItemText(0, _translate("Student_Interface", "升序"))
        self.order.setItemText(1, _translate("Student_Interface", "降序"))
        self.confirm_disp.setText(_translate("Student_Interface", "显示"))
        self.label_4.setText(_translate("Student_Interface", "展示模式"))
        self.label_12.setText(_translate("Student_Interface", "修改申请"))
        self.label_14.setText(_translate("Student_Interface", "撤销申请"))
        self.label_6.setText(_translate("Student_Interface", "离开时间"))
        self.label_7.setText(_translate("Student_Interface", "返回时间"))
        self.label_8.setText(_translate("Student_Interface", "申请理由"))
        self.new_content.setText(_translate("Student_Interface", "我想申请出校"))
        self.new_confirm.setText(_translate("Student_Interface", "确认新建"))
        self.label_9.setText(_translate("Student_Interface", "离开时间"))
        self.label_10.setText(_translate("Student_Interface", "返回时间"))
        self.label_11.setText(_translate("Student_Interface", "申请理由"))
        self.rev_content.setText(_translate("Student_Interface", "我想修改出校申请"))
        self.label_13.setText(_translate("Student_Interface", "申请编号"))
        self.rev_confirm.setText(_translate("Student_Interface", "确认修改"))
        self.label_16.setText(_translate("Student_Interface", "申请编号"))
        self.cancel_confirm.setText(_translate("Student_Interface", "确认撤销"))
        self.self_info.setHtml(_translate("Student_Interface", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'汀明体\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\'; font-size:9pt;\"><br /></p></body></html>"))
import bg_rc