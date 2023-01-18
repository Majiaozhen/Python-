import os
import tkinter
import tkinter.messagebox
def main():
    flag = open('flag')
    word = flag.read()
    if word == '0':
        print('首次启动!')
        flag.close()
        c_flag()               #首次启动后将flag置为1
        init()                 #初始化函数
        print_login_menu()     #登录菜单面板
        user_select()          #选择用户类型

    elif word == '1':
        print('欢迎回来!')
        print_login_menu()    #登录菜单面板
        user_select()         #选择用户类型
def c_flag():
    file = open('flag','w')
    file.write('1')
    file.close()

def init():
    file = open('u_root','w')
    root = {'rnum':'majiaozhen','rpwd':'123456'}
    file.write(str(root))
    file.close()
    os.mkdir('users')

def print_login_menu():
    print('----用户登录----')
    print('1-管理员登录')
    print('2-普通用户登录')
    print('----------------')
def user_select():
    global yanzheng         #创建一个全局变量，用来存储输入的内容，此处的用户类型会对后面的名片系统的菜单产生影响。
    while True:
        user_type_select = input('请选择用户类型:')
        if user_type_select == '1':
            root_login()     #进入root登录界面，验证用户名和密码
            yanzheng = 1
            break
        elif user_type_select == '2':
            print('----用户登录----')
            user_login()     #进入普通用户登录界面，验证用户名和密码
            yanzheng = 2
            break
        else:
            print('输入有误，请重新选择')
            tkinter.messagebox.showwarning('错啦', '1和2你都输入不对，你能干点啥？')
    else:
        print('初始化参数错误!')

def root_login():
    while True:
        print('****管理员登录****')
        root_number = input('请输入账户名:')   #该变量用来存储用户输入的用户名
        root_password = input('请输入密码:')   #该变量用来存储用户输入的密码
        file_root = open('u_root')          #打开root用户信息文件，用来比对用户名和密码是否正确
        root = eval(file_root.read())
        if root_number == root['rnum'] and root_password == root['rpwd']:  #用户名和密码正确
            print("登陆成功")
            tkinter.messagebox.showinfo('登录','主人，你登陆成功了呦！')
            break
        else:        #用户名和密码错误
            print("验证失败！")
            tkinter.messagebox.showwarning('警告','警告你，不要骗我，你不是主人')

def user_register():
    global us
    user_pwd = input('请输入密码:')
    user_name = input('请输入昵称:')
    user = {'u_id':us,'u_pwd':user_pwd,'u_name':user_name}
    user_path = './users/'+us  #将文件路径赋值给变量
    file_user = open(user_path,'w')
    file_user.write(str(user))
    file_user.close()

def user_login():
    while True:         #建立一个循环来使如果输入错误继续输入
        print('****普通用户登录****')
        global yhmyz           #用来验证用户名
        user_id = input('请输入账户名:')
        yhmyz = user_id
        user_pwd = input('请输入密码（若忘记密码，请联系主人修改密码哦！）:')
        user_list = os.listdir('./users')
        flag = 0
        for user in user_list:  #遍历用户名列表信息
            if user == user_id:   #验证用户名是否存在
                print('登陆中···')
                file_name = './users/'+user_id  #存储文件地址
                file_user = open(file_name)   #存储文件
                user_info = eval(file_user.read())   #读取文件信息并赋值
                if user_pwd == user_info['u_pwd']:  #验证密码是否正确
                    print("登陆成功！")
                    tkinter.messagebox.showinfo('登录',yhmyz+'，恭喜你你登陆成功了！')#弹出窗口
                    flag = 1           #设置变量以判断是否进入这段代码
                    break
        if flag == 1:
            break
        elif flag == 0:
            print("用户名或密码错误，请重新登陆！")
            tkinter.messagebox.showwarning('警告','，你的用户名或密码错误了哦，请重新登陆！')
def ycxt():
    while True:
        mm = input("请输入当前登录用户的密码：")
        if yanzheng == 1:   #管理员用户
            if mm == "123456":
                print("退出成功！")
                tkinter.messagebox.showinfo('退出', '主人，我会想你的！')
                break
            else:
                print("密码错误")
                tkinter.messagebox.showerror('错误', '咦，你在无中生有？')
        if yanzheng == 2:   #普通用户，从文件中查找密码并比对
            user_list = os.listdir('./users')
            flag = 0
            for user in user_list:
                if user == yhmyz:
                    print('退出中···')
                    file_name = './users/' + yhmyz
                    file_user = open(file_name)
                    user_info = eval(file_user.read())
                    if mm == user_info['u_pwd']:
                        print('退出系统成功!')
                        tkinter.messagebox.showinfo('退出', '欢迎下次使用！')
                        flag = 1  #看是否进入本段代码
                        break
            if flag == 1:
                break
            elif flag == 0:
                print('密码错误，请重新输入！')
                tkinter.messagebox.showerror('错误', '你在无中生有？')
def xgmm(name):
    user_id = name
    user_pwd = input('请输入要修改后的密码:')
    user_list = os.listdir('./users')
    for user in user_list:
        if user == user_id:
            file_name = './users/' + user_id
            file_user = open(file_name)
            user_info = eval(file_user.read())
            user_info['u_pwd']=user_pwd
            file_user.close()
            file_user=open(file_name,'w+')
            file_user.write(str(user_info))
            file_user.close()
    print("改密成功！")
def xgzhm(name,xm):
    user_id = name
    user_list = os.listdir('./users')
    for user in user_list:
        if user == user_id:
            file_name = './users/' + user_id
            file_user = open(file_name)
            user_info = eval(file_user.read())
            user_info['u_id'] = xm
            file_user.close()
            file_user = open(file_name, 'w+')
            file_user.write(str(user_info))
            file_user.close()
            os.rename("./users/" + user_id, "./users/" + xm)
if __name__ == '__main__':
    main()