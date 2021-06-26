from setup import *
import datetime



class student:
    def __init__(self, id: int, fn: str, ln: str, dep: int,password='0000'):
        self.id = id
        self.fn = fn
        self.ln = ln
        self.dep = dep
        self.state = False

        self.id_check ={
            'id': id,
            'password': password
        }
        sid_check_pool.append(self.id_check)

    def validate(self):
        '''插入学生'''
        if(self.state):
            print("该学生已经入学！")
            return
        else:
            _info = "('" + str(
                self.id
            ) + "', " + "'" + self.ln + "', " + "'" + self.fn + "', " + str(
                self.dep) + ")"
            _opr = 'INSERT INTO student."STUDENT" VALUES ' + _info
            _cur = conn.cursor()
            _cur.execute(_opr)
            conn.commit()
            #print(_opr + '：成功执行')
            self.state = True

    def drop(self):
        '''删除学生'''
        if(not(self.state)):
            print("该学生已经退学！")
            return
        else:
            #先从check pool 中删除
            for i in range(len(sid_check_pool)):
                if(sid_check_pool[i]['id']==self.id):
                    del sid_check_pool[i]
            #再从数据库中删除相关信息
            _id = str(self.id)
            _opr = 'DELETE FROM student."STUDENT" WHERE student_id = ' + _id
            _cur = conn.cursor()
            _cur.execute(_opr)
            conn.commit()
            print(str(self.id) + ' successfully dropped from school!')
            self.state = False

    def ins_app(self,
                leaving_t: 'in this format: 2001-09-28 23:00',
                return_t,
                content=''):
        '''提交申请'''
        complete = False
        _val = "('" + leaving_t + "', " + "'" + return_t + "', " + "'" + content + "', " + str(
            self.id) + ", 'Pending'" ")"
        #print(_val)
        _opr = 'INSERT INTO public."APPLICATION"(leaving_t,return_t, content, "student_id_STUDENT", state ) VALUES ' + _val
        #print(_opr)
        _cur = conn.cursor()
        _cur.execute(_opr)

        if (self.__max_app() or self.__overlap() or self.__max_leaving()
                or self.__cross()):
            conn.rollback()
            return 1
        else:
            complete = True
            conn.commit()

        if (complete):
            _cur2 = conn.cursor()
            _cur2.execute(
                'SELECT ap.application_id FROM public."APPLICATION" ap WHERE ap.application_id not in (SELECT vt."application_id_APPLICATION" FROM public."VETTING" vt)'
            )
            app_id = list(_cur2)
            if (len(app_id) > 1):
                print('Application number error!')
                return

            _cur3 = conn.cursor()
            _cur3.execute(
                'INSERT INTO public."VETTING"(time, "application_id_APPLICATION") VALUES (%s,%s)',
                (str(datetime.datetime.now()), str(app_id[0][0])))
            conn.commit()
            return 0

    def sort_by_time(self, asc=True):
        '''按时间排序'''
        _curAp = conn.cursor()
        if (asc):
            _curAp.execute(
                'SELECT app.application_id, app.leaving_t, app.return_t, app.state, app.content, vt.comment AS Vetting_Comment, vt.time AS Comment_Time FROM (public."APPLICATION" app LEFT JOIN public."VETTING" vt ON vt."application_id_APPLICATION" = app.application_id) WHERE "student_id_STUDENT" = %s ORDER BY leaving_t ASC',
                (str(self.id), ))
        else:
            _curAp.execute(
                'SELECT app.application_id, app.leaving_t, app.return_t, app.state, app.content, vt.comment AS Vetting_Comment, vt.time AS Comment_Time FROM (public."APPLICATION" app LEFT JOIN public."VETTING" vt ON vt."application_id_APPLICATION" = app.application_id) WHERE "student_id_STUDENT" = %s ORDER BY leaving_t DESC',
                (str(self.id), ))

        return list(_curAp)

        #for row in _curAp:
            #print(row)
            #TODO:补充comment

    def sort_by_state(self, state='Pending'):
        '''选取特定状态的申请'''
        _cur = conn.cursor()
        _cur.execute(
                'SELECT app.application_id, app.leaving_t, app.return_t, app.state, app.content, vt.comment AS Vetting_Comment, vt.time AS Comment_Time FROM (public."APPLICATION" app LEFT JOIN public."VETTING" vt ON vt."application_id_APPLICATION" = app.application_id) WHERE "student_id_STUDENT" = %s  AND app.state= %s ORDER BY app.leaving_t ASC',
            (self.id, state.capitalize()))
        #TODO:补充comment

        return list(_cur)

    def revise(self, app_id, leaving_t, return_t, content=''):
        '''修改申请时间'''
        complete = False  #修改结果
        #确认student_id
        _cur1 = conn.cursor()
        _cur1.execute(
            'SELECT application_id FROM public."APPLICATION" WHERE "student_id_STUDENT" = %s',
            (str(self.id), ))
        cur_list = list(_cur1)
        id_list = list()
        for i in cur_list:
            id_list.append(i[0])

        if (not (app_id in id_list)):
            print("你没有该申请号的申请")
            return 2

        #确认申请状态

        _cur2 = conn.cursor()
        _cur2.execute(
            'SELECT state FROM public."APPLICATION" WHERE application_id = %s',
            (str(app_id), ))
        state = list(_cur2)[0][0]
        if (not (state == 'Passed') and not (state == 'Refused')):
            print("你只能修改通过的或已被拒绝的申请！")
            return 3

        #执行UPDATE
        _cur = conn.cursor()
        _cur.execute(
            'UPDATE public."APPLICATION" SET leaving_t = %s, return_t = %s, content = %s, state = %s WHERE application_id = %s',
            (leaving_t, return_t, content, 'Pending', str(app_id)))
        if (self.__max_app() or self.__overlap() or self.__max_leaving()
                or self.__cross()):
            conn.rollback()
            return 1
        else:
            complete = True
            conn.commit()
        #新建vetting关系
        if (complete):
            _cur3 = conn.cursor()
            _cur3.execute(
                'INSERT INTO public."VETTING"(time, "application_id_APPLICATION") VALUES (%s,%s)',
                (str(datetime.datetime.now()), str(app_id)))
            conn.commit()
            return 0

    def cancel(self, app_id):
        #确认student_id
        _cur1 = conn.cursor()
        _cur1.execute(
            'SELECT application_id FROM public."APPLICATION" WHERE "student_id_STUDENT" = %s',
            (str(self.id), ))
        cur_list = list(_cur1)
        id_list = list()
        for i in cur_list:
            id_list.append(i[0])

        if (not (app_id in id_list)):
            print("你没有该申请号的申请")
            return 2

        #执行删除
        _cur = conn.cursor()
        _cur.execute(
            'UPDATE public."APPLICATION" SET state = %s WHERE application_id = %s',
            ('Cancelled', str(app_id)))
        conn.commit()
        return 0

    def self_info(self):
        cur = conn.cursor()
        cur.execute('SELECT student_id, last_name, first_name, d.name FROM student."STUDENT" s Join public."DEPARTMENT" d on s."department_id_DEPARTMENT"  = d.department_id WHERE student_id = %s',(str(self.id), ))
        return list(cur)

    def __overlap(self):
        '''重叠？'''
        _cur = conn.cursor()
        _cur.execute(
            'SELECT leaving_t, return_t FROM public."APPLICATION" WHERE "student_id_STUDENT" = %s and state!= %s',
            (str(self.id), 'Cancelled'))
        x = list(_cur)
        for i in range(len(x)):
            for j in range(len(x)):
                if ((((x[i][0] >= x[j][0]) and (x[i][0] <= x[j][1])) or
                     ((x[i][1] >= x[j][0]) and (x[i][1] <= x[j][1])))
                        and (i != j)):
                    print("时间有重叠！")
                    return True

    def __cross(self):
        '''时间交叉'''
        _cur = conn.cursor()
        _cur.execute(
            'SELECT leaving_t, return_t FROM public."APPLICATION" WHERE "student_id_STUDENT" = %s',
            (str(self.id), ))
        x = list(_cur)
        for i in range(len(x)):
            if (x[i][0] >= x[i][1]):
                print("返回时间需要晚于离开时间！")
                return True

    def __max_leaving(self):
        '''最多离开两天'''
        _cur = conn.cursor()
        _cur.execute(
            'SELECT leaving_t, return_t FROM public."APPLICATION" WHERE "student_id_STUDENT" = %s',
            (str(self.id), ))
        x = list(_cur)
        for i in range(len(x)):
            if (x[i][1] - x[i][0] > datetime.timedelta(days=2)):
                print("最多离开两天！")
                return True


    def __max_app(self):
        '''最多三个申请'''
        _cur = conn.cursor()
        _cur.execute(
            'SELECT leaving_t FROM public."APPLICATION" WHERE "student_id_STUDENT" = %s and state != %s ORDER BY leaving_t',
            (str(self.id), 'Cancelled'))
        x = list(_cur)
        time_list = list()
        for i in range(len(x)):
            time_list.append(x[i][0])
        #print(time_list)
        for i in range(len(time_list)):
            count = 0
            for j in range(i, len(time_list)):
                if (time_list[j] < time_list[i] + datetime.timedelta(days=7)):
                    count += 1
            if (count > 3):
                print("一周最多出去三次！")
                return True


lqz = student(2019011950, '刘', '綦泽', 2, password='qwert')
zhangsan = student(2019011000,'张','三',2,password='0000')
lisi = student(2019011001,'李','四',2,password='1234')
wangwu = student(2019011002,'王','五',1,password='1111')
zhaoliu = student(2019011003,'赵', '六',3,password='7890')
student_pool = [lqz,zhangsan,lisi,wangwu,zhaoliu]

if __name__ == '__main__':
    for student in student_pool:
        student.validate()

    cur = conn.cursor()
    cur.execute('SELECT * FROM student."STUDENT"')
    for row in cur:
        print(row)

ruozhi = student(2019011950,'弱','智','Department of Industrial Engineering')