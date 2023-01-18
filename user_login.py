import os
def main():
    flag = open('flag')
    word = flag.read()
    if word == '0':
        print('首次启动!')
        flag.close()
        c_flag()
        init()
        print_login_menu()
        user_select()

    elif word == '1':
        print('欢迎回来!')
        print_login_menu()
        user_select()
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
    while True:
        user_type_select = input('请选择用户类型:')
        if user_type_select == '1':
            root_login()
            break
        elif user_type_select == '2':
            while True:
                select = input('是否需要注册?(y/n):')
                if select.lower() == 'y':
                    print('----用户注册----')
                    user_register()
                    break
                elif select.lower() == 'n':
                    print('----用户登录----')
                    break
                else:
                    print('输入有误，请重新选择')
            user_login()
            break
        else:
            print('输入有误，请重新选择')
    else:
        print('初始化参数错误!')


def root_login():
    while True:
        print('****管理员登录****')
        root_number = input('请输入账户名:')
        root_password = input('请输入密码:')
        file_root = open('u_root')
        root = eval(file_root.read())
        if root_number == root['rnum'] and root_password == root['rpwd']:
            print('登陆成功!')
            break
        else:
            print('验证失败!')

def user_register():
    user_id = input('请输入账户名:')
    user_pwd = input('请输入密码:')
    user_name = input('请输入昵称:')
    user = {'u_id':user_id,'u_pwd':user_pwd,'u_name':user_name}
    user_path = './users/'+user_id
    file_user = open(user_path,'w')
    file_user.write(str(user))
    file_user.close()

def user_login():
    while True:
        print('****普通用户登录****')
        user_id = input('请输入账户名:')
        user_pwd = input('请输入密码:')
        user_list = os.listdir('./users')
        flag = 0
        for user in user_list:
            if user == user_id:
                flag = 1
                print('登陆中···')
                file_name = './users/'+user_id
                file_user = open(file_name)
                user_info = eval(file_user.read())
                if user_pwd == user_info['u_pwd']:
                    print('登陆成功!')
                    break
        if flag == 1:
            break
        elif flag == 0:
            print('查无此人!请先注册用户')
            break



if __name__ == '__main__':
    main()