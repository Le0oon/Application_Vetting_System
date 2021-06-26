import psycopg2

sid_check_pool = list()
tid_check_pool = list()



def t_config(id,psw):
    for i in range(len(tid_check_pool)):
        if(tid_check_pool[i]['id'] == id):
            if(tid_check_pool[i]['password'] == psw):
                return True  #密码正确
            else:
                return False #密码错误
    return False #未找到用户，返回F

def s_config(id,psw):
    print(sid_check_pool)
    for i in range(len(sid_check_pool)):
        if(sid_check_pool[i]['id'] == id):
            if(sid_check_pool[i]['password'] == psw):
                return True #密码正确
            else:
                return False #密码错误
    return False #未找到用户，返回F




conn = psycopg2.connect("dbname=SMS_new user=postgres password=dress768596")

