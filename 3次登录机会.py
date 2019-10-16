# _*_ encoding=utf-8 _*_
import hashlib
import re
import  os
import json
file_path = r'C:\Users\Administrator\Desktop\Python-100-Days-master\python_practice\day10\login\user'

class User():

    def main(self):
        print('====会员登录系统1.1')
        print('1=====会员登录=====')
        print('2=====会员注册=====')
        # print('3=====忘记密码=====')
        print('请选择功能')
        number = input()
        if number == str(1) :
            self.login()
        elif number == str(2):
            self.register()
        # elif number == 3:#留着以后该密码使用

        #     pass
        else:
            print('输入错误请重试')

    def login(self):
        '三次登录录功能'
        i = 3#初始话有几次输入机会
        while True:#死循环一定要注意缩进，代码块等
            print('登录有三次机会，还剩%i机会'%i)
            if i == 0 :
                break
            # lis = []
            print('======登录=======')
            user_name=input('请输入用户名')
            passwd = input('请输入密码')
            passwd=self.encrypt(passwd)
            lis_emp = self.read_date()#返回users的列表
            # print(lis_emp)
            if lis_emp  ==[]:
                print('数据为空...,请先注册...')
                self.register()
                break
            #检查用户名是否存在
            for emp in  lis_emp:
                emp = json.loads(emp)
                if user_name == emp['user_name'] and  passwd == emp['passwd']:#遍历对比，有么有注册过用户名

                    print('欢迎回来%s'%user_name)
                    self.user_set()
                    return
            else:
                i -=1
                print('用户名或密码错误,请重试')
                continue

    def register(self):
        '注册功能'
        active = True
        print('======注册功能=======')
        while active:
            user_name = input('请输入用户名:(按q/Q退出)')
            lis_emp=self.read_date()#返回用户列表
            # print(lis_emp)
            if user_name.upper().strip() =='Q':
                break
            for emp in  lis_emp[:]:
                emp = json.loads(emp)
                if emp['user_name'] == user_name:
                    print('已经存在用户，请尝试其他用户名')
                    break
            else:#列表还没有用户，注册
                passwd = input('请输入密码')#
                if self.check_passwd(passwd):
                    passwd=self.encrypt(passwd)
                    self.write_date(user_name,passwd)#将用户名和加密过的密码存入文件中
                    print('注册成功！，请重新登录')
                    break
                else:
                    print('密码必须包含一个小写字母，且长度为8-16位')
                    break

    def check_passwd(self,passwd):
        '检测密码，是否合格...'
        regex=re.compile('^(?=.*[a-z])[\w~!@&%#_\.]{8,16}$')
        if regex.match(passwd):
            return True
        else:
            # print('密码必须一个小写字母，且密码长度为8-16位')
            return False

    def encrypt(self,passwd):
        '加密密码'
        s = hashlib.md5()
        s.update(passwd.encode())
        passwd = s.hexdigest()
        return passwd

    def read_date(self):
        lis = []
        with open(file_path,'r') as f :
            for emp in f:#遍历每个对象
                lis.append(emp.strip())
        return  lis

    def write_date(self,user_name,passwd):
        '写用户数据到文件中'
        user_dic = {}
        user_dic['user_name'] = user_name
        user_dic['passwd']    = passwd
        # print(User.check_id())#这里为啥为零啊，草哎
        # user_dic['id'] = User.id_index()
        user_dic['id']  = User.check_id()+1
        user_str = json.dumps(user_dic,ensure_ascii=False)
        if user_dic['id']==1:
            with open(file_path,'a') as f :
                f.write(user_str)
        else:
            with open(file_path,'a') as f:#先换行，在写数据
                f.write('\n')
                f.write(user_str)

    @staticmethod#静态方法，类似于函数，只是在类的管理下类可以调用
    def check_id():#从文件中获取id
        with open(file_path, 'r' )as f:
            # for line in f:#假如文件不读一遍，就会出问题，指针不能定位，文件不读一遍怎么会知道字符串的位置
            #     pass
            f.read()
            #     # print(line.strip())
            # # print(f.tell())
            try:#假如第一次注册，就把id设置成1
                f.seek((int(f.tell()) - 2), 0)#设置指针
                kk = f.read()#读指针后面的内容  为 id} id是我们要的字符窜
                print(kk)
                id_ = int(kk[0])#取字符串id转换成数字类型
            except ValueError :
                id_=0
            return id_##

    def user_set(self):
        print('会员功能')
        print('修改密码')
        print('修改用户名')

    def yzm(self):
        '验证码...'
        pass


if __name__ == '__main__':
    u = User()
    while True:
        u.main()
