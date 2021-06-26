from setup import *
from student import student
import numpy as np
import datetime


class teacher:
    def __init__(self, id, fn, ln, dep,password='0000'):
        self.id = id
        self.fn = fn
        self.ln = ln
        self.dep = dep
        self.state = False
        self.id_check = {
            'id': id,
            'password': password
        }
        tid_check_pool.append(self.id_check)

    def validate(self):
        '''插入老师'''
        if (self.state):
            print("该教师已经在职！")
            return
        else:
            _info = "('" + str(
                self.id
            ) + "', " + "'" + self.fn + "', " + "'" + self.ln + "', " + str(
                self.dep) + ")"
            _opr = 'INSERT INTO teacher."TEACHER" VALUES ' + _info
            _cur = conn.cursor()
            _cur.execute(_opr)
            conn.commit()
            self.state = True
            # print(_opr + '：成功执行')

    def drop(self):
        '''删除教师'''
        if (not (self.state)):
            print("该教师已经退出！")

            return
        else:
            # 先从check pool 中删除
            for i in range(len(tid_check_pool)):
                if (tid_check_pool[i]['id'] == self.id):
                    del tid_check_pool[i]
            # 再从数据库中删除相关信息
            _id = str(self.id)
            _opr = 'DELETE FROM teacher."TEACHER" WHERE teacher_id = ' + _id
            _cur = conn.cursor()
            _cur.execute(_opr)
            conn.commit()
            print(str(self.id) + ' successfully dropped from school!')
            self.state = False

    def sort_by_time(self, asc=True, whole_dep_app=True):
        '''按时间排序，可选显示院系全部申请或本人审批的申请'''

        _cur = conn.cursor()
        if (whole_dep_app):
            if (asc):
                _cur.execute(
                    'SELECT app.application_id, app.leaving_t, app.return_t, app.state, app.content, vt.comment, app."student_id_STUDENT", vt.time, vt."teacher_id_TEACHER" FROM (public."APPLICATION" app LEFT JOIN public."VETTING" vt ON vt."application_id_APPLICATION" = app.application_id) WHERE app."student_id_STUDENT" in (SELECT s.student_id FROM student."STUDENT" s WHERE s."department_id_DEPARTMENT" in (SELECT "department_id_DEPARTMENT" FROM teacher."TEACHER" t WHERE t.teacher_id = %s)) ORDER BY leaving_t ASC',
                    (str(self.id),))
            else:
                _cur.execute(
                    'SELECT app.application_id, app.leaving_t, app.return_t, app.state, app.content, vt.comment, app."student_id_STUDENT", vt.time, vt."teacher_id_TEACHER" FROM (public."APPLICATION" app LEFT JOIN public."VETTING" vt ON vt."application_id_APPLICATION" = app.application_id) WHERE app."student_id_STUDENT" in (SELECT s.student_id FROM student."STUDENT" s WHERE s."department_id_DEPARTMENT" in (SELECT "department_id_DEPARTMENT" FROM teacher."TEACHER" t WHERE t.teacher_id = %s)) ORDER BY leaving_t DESC',
                    (str(self.id),))
        else:
            if (asc):
                _cur.execute(
                    'SELECT ap.application_id, ap.leaving_t, ap.return_t, ap.state, ap.content, vt.comment, ap."student_id_STUDENT", vt.time, vt."teacher_id_TEACHER" FROM (public."APPLICATION" ap LEFT JOIN public."VETTING" vt ON vt."application_id_APPLICATION" = ap.application_id) WHERE ap.application_id in (SELECT "application_id_APPLICATION" FROM  public."VETTING" WHERE "teacher_id_TEACHER" = %s) ORDER BY leaving_t ASC',
                    (str(self.id),))
            else:
                _cur.execute(
                    'SELECT app.application_id, app.leaving_t, app.return_t, app.state, app.content, vt.comment,app."student_id_STUDENT", vt.time, vt."teacher_id_TEACHER" FROM (public."APPLICATION" ap LEFT JOIN public."VETTING" vt ON vt."application_id_APPLICATION" = ap.application_id) WHERE ap.application_id in (SELECT "application_id_APPLICATION" FROM  public."VETTING" WHERE "teacher_id_TEACHER" = %s) ORDER BY leaving_t DESC',
                    (str(self.id),))

        return list(_cur)
            # TODO:补充comment

    def sort_by_state(self, state='Pending', whole_dep_app=True):
        '''选取本院系特定状态的申请,可选显示院系全部申请或本人审批的申请'''
        _cur = conn.cursor()
        if (whole_dep_app):
            _cur.execute(
                'SELECT ap.application_id, ap.leaving_t, ap.return_t, ap.state, ap.content, vt.comment, ap."student_id_STUDENT", vt.time, vt."teacher_id_TEACHER" FROM (public."APPLICATION" ap LEFT JOIN public."VETTING" vt ON vt."application_id_APPLICATION" = ap.application_id) WHERE ap."student_id_STUDENT" in (SELECT s.student_id FROM student."STUDENT" s WHERE s."department_id_DEPARTMENT"  in (SELECT "department_id_DEPARTMENT" FROM teacher."TEACHER" t WHERE t.teacher_id = %s)) AND state = %s',
                (self.id, state.capitalize()))
        else:
            _cur.execute(
                'SELECT ap.application_id, ap.leaving_t, ap.return_t, ap.state, ap.content, vt.comment, ap."student_id_STUDENT", vt.time, vt."teacher_id_TEACHER" FROM (public."APPLICATION" ap LEFT JOIN public."VETTING" vt ON vt."application_id_APPLICATION" = ap.application_id) WHERE ap.application_id in (SELECT "application_id_APPLICATION" FROM  public."VETTING" WHERE "teacher_id_TEACHER" = %s) AND state = %s',
                (self.id, state.capitalize()))
        # TODO:补充comment

        return list(_cur)

    def vet_app(self, app_id, passed=True, comment=''):
        '''审批'''
        if (self.__accessible(app_id)):
            # print('开始修改')
            _cur = conn.cursor()
            if (passed):
                _cur.execute(
                    'UPDATE public."APPLICATION" SET state = %s WHERE application_id = %s',
                    ('Passed', str(app_id)))
                conn.commit()
                # print('同意')
            else:
                _cur.execute(
                    'UPDATE public."APPLICATION" SET state = %s WHERE application_id = %s',
                    ('Refused', str(app_id)))
                conn.commit()
            self.record_vet_comment(app_id, comment)
            return 0

        else:
            print("只能审批本院系的学生！")
            return 1



    def record_vet_comment(self, app_id, comment):
        _cur = conn.cursor()
        _cur.execute(
            'SELECT vetting_id FROM public."VETTING" WHERE "application_id_APPLICATION" = %s ORDER BY time DESC',
            (str(app_id),))
        vet_id = list(_cur)[0][0]

        _cur1 = conn.cursor()
        _cur1.execute(
            'UPDATE public."VETTING" SET comment = %s, time = %s, "teacher_id_TEACHER" = %s WHERE vetting_id = %s',
            (comment, str(datetime.datetime.now()), str(self.id), str(vet_id)))
        conn.commit()

    def self_info(self):
        cur = conn.cursor()
        cur.execute(
            'SELECT teacher_id,first_name, last_name, d.name FROM teacher."TEACHER" t Join public."DEPARTMENT" d on t."department_id_DEPARTMENT"  = d.department_id WHERE teacher_id = %s',
            (str(self.id),))
        return list(cur)

    def __accessible(self, app_id):
        '''返回是否可以审批某条app_id的申请'''
        _cur = conn.cursor()
        _cur.execute(
            'SELECT application_id FROM public."APPLICATION" WHERE "student_id_STUDENT" in (SELECT s.student_id FROM student."STUDENT" s WHERE s."department_id_DEPARTMENT"  in (SELECT "department_id_DEPARTMENT" FROM teacher."TEACHER" t WHERE t.teacher_id = %s))',
            (str(self.id),))
        app_list = np.array(list(_cur))[:, 0]
        if (app_id in app_list):
            return True
        else:
            return False



zl = teacher(100,'Zheng ', 'Li',2,password='12345678')
zxb = teacher(101,'Zhao ','Xb',2,password='qwert')
lys = teacher(102,'李','岩松',1,password='FenLiGuaKe')
rd = teacher(103,'阮','东', 1,password='ZiXinZhuDongJiaoLiu')
lm = teacher(104,'Li ','Ming',3,password='1234')

teacher_pool = [zl,zxb,lys,rd,lm]

if __name__ == '__main__':
    for teacher in teacher_pool:
        teacher.validate()

    cur = conn.cursor()
    cur.execute('SELECT * FROM teacher."TEACHER"')
    for row in cur:
        print(row)



