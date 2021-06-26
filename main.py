from student import *
from teacher import *
from setup import *
import sys
from datetime import datetime

import re
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Login import *
from student_ui import *
from teacher_ui import *
from error_ui import *

# student类




class myMainWin(QMainWindow, Ui_MainWindow):
    window=list()
    def __init__(self,parent = None):
        super(myMainWin, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('登陆')
        self.confirm.clicked.connect(self.check_config)

    def check_config(self):
        user_id = int(self.id_input.text())
        user_psw = self.psw_input.text()
        if(self.type_input.currentIndex()):
            '''教师登陆'''
            if (t_config(user_id,user_psw)):
                print("Successfully logged in!")
                #创建教师界面
                myTWin = myTeacher(tid=user_id)
                self.window.append(myTWin)
                myTWin.show()
            else:
                myErrorWin = Error_info(error_info='您的用户名或密码错误！请重试！')
                self.window.append(myErrorWin)
                myErrorWin.show()
        else:
            '''学生登陆'''
            if (s_config(user_id, user_psw)):
                print("Successfully logged in!")
                # 创建学生界面
                mySWin = myStudent(sid=user_id)
                self.window.append(mySWin)
                mySWin.show()

            else:
                myErrorWin = Error_info(error_info='您的用户名或密码错误！请重试！')
                self.window.append(myErrorWin)
                myErrorWin.show()


class myStudent(QMainWindow, Ui_Student_Interface):
    window = list()
    def __init__(self,parent = None,sid = 0):
        super(myStudent, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(str(sid))
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.verticalHeader().setVisible(False)
        for i in range(len(student_pool)):
            if(student_pool[i].id == sid):
                self.stu = student_pool[i]
        self.confirm_disp.clicked.connect(self.call_table)
        self.new_confirm.clicked.connect(self.call_ins_app)
        self.rev_confirm.clicked.connect(self.call_revise)
        self.cancel_confirm.clicked.connect(self.call_cancel)

        info = self.stu.self_info()
        raise_info = '你好：' + info[0][2] + info[0][1] + ' 同学！\t你的学号为: ' + str(info[0][0]) + '\t 你所在院系为：' + info[0][3]
        self.self_info.setText(raise_info)


        #insert into table

    def call_table(self):
        self.tableWidget.clearContents()
        if(self.state.currentIndex()==0):
            if(self.order.currentIndex()):
                items = self.stu.sort_by_time(asc=True)
            else:
                items = self.stu.sort_by_time(asc=True)[::-1]
        elif(self.state.currentIndex()==1):
            if(self.order.currentIndex()):
                items = self.stu.sort_by_state()
            else:
                items = self.stu.sort_by_state()[::-1]
        elif(self.state.currentIndex()==2):
            if (self.order.currentIndex()):
                items = self.stu.sort_by_state('Passed')
            else:
                items = self.stu.sort_by_state('Passed')[::-1]
        elif (self.state.currentIndex() == 3):
            if (self.order.currentIndex()):
                items = self.stu.sort_by_state('Refused')
            else:
                items = self.stu.sort_by_state('Refused')[::-1]
        elif (self.state.currentIndex() == 4):
            if (self.order.currentIndex()):
                items = self.stu.sort_by_state('Cancelled')
            else:
                items = self.stu.sort_by_state('Cancelled')[::-1]
        self.insert_item(items)

    def insert_item(self,items):
        for i in range(len(items)):
            item = items[i]
            row = 0
           #row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            for j in range(len(item)):
                item = QTableWidgetItem(str(items[i][j]))
                self.tableWidget.setItem(row, j, item)

    def call_ins_app(self):
        leaving_t = self.new_leaving.dateTime().toString('yyyy-MM-dd hh:mm')
        return_t = self.new_return.dateTime().toString('yyyy-MM-dd hh:mm')
        content = self.new_content.text()
        #print(leaving_t)
        self.error_disp(self.stu.ins_app(leaving_t=leaving_t,return_t = return_t,content=content))
        self.call_table()

    def call_revise(self):
        app_id = int(self.rev_app_id.text())
        leaving_t = self.rev_leaving.dateTime().toString('yyyy-MM-dd hh:mm')
        return_t = self.rev_return.dateTime().toString('yyyy-MM-dd hh:mm')
        content = self.rev_content.text()
        self.error_disp(self.stu.revise(app_id=app_id, leaving_t = leaving_t, return_t = return_t, content=content))
        #print("success")
        self.call_table()

    def call_cancel(self):
        app_id = int(self.cancel_app_id.text())
        self.error_disp(self.stu.cancel(app_id=app_id))
        self.call_table()

    def error_disp(self,error_type):
        '''报错提示'''
        if error_type ==0:
            return
        elif error_type == 1:
            info = '申请无效：\n \t请检查时间是否重叠；\n \t七天内出入是否超过3次; \n\t出校时间是否超过48小时;'
        elif error_type == 2:
            info = '你没有该申请号的申请!'
        elif error_type == 3:
            info = '你只能修改通过的或已被拒绝的申请!'

        myErrorWin = Error_info(error_info=info)
        self.window.append(myErrorWin)
        myErrorWin.show()


                        


class myTeacher(QMainWindow, Ui_Teacher_Interface):
    window = list()
    def __init__(self,parent = None,tid = 0):
        super(myTeacher, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle(str(tid))
        for i in range(len(teacher_pool)):
            if(teacher_pool[i].id == tid):
                self.tea = teacher_pool[i]
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.verticalHeader().setVisible(False)

        self.confirm_disp.clicked.connect(self.call_table)
        self.confirm.clicked.connect(self.call_vet_app)

        info = self.tea.self_info()
        raise_info = '您好：' + info[0][1] + info[0][2] + ' 老师！\t您的教师编号为: ' + str(info[0][0]) + '\t您所在院系为：' + info[0][3]
        self.self_info.setText(raise_info)


    def call_table(self):
        self.tableWidget.clearContents()
        #print(str(self.order.currentIndex()) + str(self.state.currentIndex())+ str(self.whole_dep.currentIndex()))
        if self.order.currentIndex()==0:
            if self.state.currentIndex()==0:
                items = self.tea.sort_by_time(whole_dep_app = bool(self.whole_dep.currentIndex()))
            elif self.state.currentIndex()==1:
                items = self.tea.sort_by_state(whole_dep_app=bool(self.whole_dep.currentIndex()), state='Pending')
            elif self.state.currentIndex()==2:
                items = self.tea.sort_by_state(whole_dep_app=bool(self.whole_dep.currentIndex()), state='Passed')
            elif self.state.currentIndex()==3:
                items = self.tea.sort_by_state(whole_dep_app=bool(self.whole_dep.currentIndex()), state='Refused')
            elif self.state.currentIndex()==4:
                items = self.tea.sort_by_state(whole_dep_app=bool(self.whole_dep.currentIndex()), state='Cancelled')
        else:
            if self.state.currentIndex() == 0:
                items = self.tea.sort_by_time(whole_dep_app=bool(self.whole_dep.currentIndex()))[::-1]
            elif self.state.currentIndex() == 1:
                items = self.tea.sort_by_state(whole_dep_app=bool(self.whole_dep.currentIndex()), state='Pending')[::-1]
            elif self.state.currentIndex() == 2:
                items = self.tea.sort_by_state(whole_dep_app=bool(self.whole_dep.currentIndex()), state='Passed')[::-1]
            elif self.state.currentIndex() == 3:
                items = self.tea.sort_by_state(whole_dep_app=bool(self.whole_dep.currentIndex()), state='Refused')[::-1]
            elif self.state.currentIndex() == 4:
                items = self.tea.sort_by_state(whole_dep_app=bool(self.whole_dep.currentIndex()), state='Cancelled')[::-1]






        self.insert_item(items)

    def insert_item(self, items):
        for i in range(len(items)):
            item = items[i]
            row = 0
            # row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            for j in range(len(item)):
                item = QTableWidgetItem(str(items[i][j]))
                self.tableWidget.setItem(row, j, item)

    def call_vet_app(self):
        a_id = int(self.app_id.text())
        cmt = self.comment.text()
        print(cmt)
        if(self.tea.vet_app(app_id=a_id, passed= bool(self.result.currentIndex()), comment= cmt)):
            myErrorWin = Error_info(error_info='该学生不属于您的院系，您只能审批本院系的学生！')
            self.window.append(myErrorWin)
            myErrorWin.show()

        self.call_table()





class Error_info(QMainWindow, Ui_ErrorWin):
    def __init__(self,parent = None,error_info=''):
        super(Error_info, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('Error Information')
        self.error_info.setText(error_info)
        self.error_info.setReadOnly(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = myMainWin()
    myWin.show()
    sys.exit(app.exec_())

