import user
import os
import tkinter
import tkinter.messagebox

def dqwj():
    mp = open('mp.txt', 'r')
    for line in mp:
        d = {}
        line = line.replace("\n", '')
        v = line.split('\t')
        v1=v[0].split(':')
        v2=v[1].split(':')
        v3=v[2].split(':')
        d[v1[0]] = v1[1]
        d[v2[0]] = v2[1]
        d[v3[0]] = v3[1]
        l.append(d)
    mp.close()
def caidan():
    print("**公司名片管理系统**")
    print("1.添加名片")
    print("2.删除名片")
    print("3.修改名片")
    print("4.查询名片")
    print("5.获取所有名片信息")
    print("6.保存并读取")
    print("7.退出系统")
def tjmp():
    nn=0
    nn2=0
    nn3=0
    d={}
    name=input("请输入要增加的名字：")
    for i in l:
        if i["name"] == name:
            nn=1
            print("改员工已经添加，如果为重名，请在姓名后面添加数字以区别！")
    if nn == 0:
        while True:
            age=input("请输入要增加的年龄：")
            if int(age)>0 and int(age)<=100:
                nn3=1
            else:
                print("请输入1~100之间的整数")
                continue
            tell=input("请输入要增加的电话：")
            if tell.isdigit():
                if len(tell) == 11:
                    nn2 = 1
                    break
                else:
                    print("请输入11位数字！")
            else:
                print("请输入11位数字！")
        if nn2==1 and nn3==1:
            print("请为添加的员工注册账户：")
            user.us = name
            user.user_register()
            d["name"] = name
            d["age"] = age
            d["tell"] = tell
            l.append(d)
            print("员工添加成功！")
def scmp():
    print("注意！您正在进行删除操作，删除后该名片及账户都会被删除！")

    name=input("请输入要删除的人的姓名：")
    a=0
    for i, x in enumerate(l):
        if name == x["name"]:
            l.pop(i)
            os.remove('./users/' + name)
            print(name,"已经删除成功！")
            a=1
            break
    if a == 0:
        print("输入姓名不存在！")
def scmp2():
    print("注意！您正在进行删除操作，删除后该名片及账户都会被删除！")

    global sc
    a=0
    for i, x in enumerate(l):
        if user.yhmyz == x["name"]:
            name2 = l.pop(i)
            sc=1
            print(name2,"已经删除成功！")
            a=1
            break
    if a == 0:
        print("输入姓名不存在！")
def xgmp():
    name=input("请输入你要修改的员工姓名：")
    d={}
    n4=1
    n5=1
    for i, x in enumerate(l):
        if name == x["name"]:
            n5=0
            n3=input("您要修改姓名(注意！姓名与登录账户名会同步修改！)，年龄，还是电话，还是密码？")
            if n3=="年龄":
                age=input("请输入修改后的年龄：")
                if int(age) > 0 and int(age) <= 100:
                    d["name"] = x["name"]
                    d["age"] = age
                    d["tell"] = x["tell"]
                else:
                    print("请输入1~100之间的整数")
                    n4 = 0
            elif n3 == "姓名":
                xm = input("请输入修改后的员工姓名：")
                d["name"] = xm
                d["age"] = x["age"]
                d["tell"] = x["tell"]
                user.xgzhm(name, xm)
            elif n3 == "电话":
                tell=input("请输入修改后的电话：")
                if tell.isdigit():
                    if len(tell) == 11:
                        d["name"] = x["name"]
                        d["age"] = x["age"]
                        d["tell"] = tell
                    else:
                        print("请输入11位数字！")
                        n4 = 0
                else:
                    print("请输入11位数字！")
                    n4 = 0
            elif n3 == "密码":
                user.xgmm(name)
                n4=0
            else:
                print("输入有误！")
                n4=0
            if  n4==1:
                l[i]=d
                print("修改成功！")
    if n5==1:
        print("无此人或此人未保存")
def xgmp2():
    d={}
    n4=1
    n5=1
    for i, x in enumerate(l):
        if user.yhmyz == x["name"]:
            n5=0
            n3=input("您要修改姓名，年龄，还是电话，还是密码？")
            if n3 == "年龄":
                age = input("请输入修改后的年龄：")
                if int(age) > 0 and int(age) <= 100:
                    d["name"] = x["name"]
                    d["age"] = age
                    d["tell"] = x["tell"]
                else:
                    print("请输入1~100之间的整数")
                    n4 = 0
            elif n3 == "姓名":
                print("由于姓名与账户名绑定同步修改，请联系管理员修改！")
                n4 = 0
            elif n3 == "电话":
                tell = input("请输入修改后的电话：")
                if tell.isdigit():
                    if len(tell) == 11:
                        d["name"] = x["name"]
                        d["age"] = x["age"]
                        d["tell"] = tell
                    else:
                        print("请输入11位数字！")
                        n4 = 0
                else:
                    print("请输入11位数字！")
                    n4 = 0
            elif n3 == "密码":
                ysmm = input("请输入原始密码：")
                user_list = os.listdir('./users')
                file_name = './users/' + user.yhmyz
                file_user = open(file_name)
                user_info = eval(file_user.read())
                file_user.close()
                for u3 in user_list:
                    if u3 == user.yhmyz:
                        if ysmm == user_info["u_pwd"]:
                            user.xgmm(user.yhmyz)
                        else:
                            print("原始密码错误！")
                n4=0
            else:
                print("输入有误！")
                n4=0
            if  n4==1:
                l[i]=d
                print("修改成功！")
    if n5==1:
        print("您已经被删除")
def cxmp():
    name=input("请输入你想查询的姓名：")
    a=0
    for x in l:
        if name==x["name"]:
            print(name, "的年龄是：", x["age"])
            print(name, "的电话是：", x["tell"])
            a=1
            break
    if a == 0:
        print("输入姓名不存在！")
def cxmp2():
    for x in l:
        if user.yhmyz == x["name"]:
            print(user.yhmyz, "的年龄是：", x["age"])
            print(user.yhmyz, "的电话是：", x["tell"])
            a = 1
            break
def hqsympxx():
    for i in l:
        print(i["name"], "的年龄是：", i["age"],"\t",i["name"], "的电话是：", i["tell"])
def wdic():
    with open('./mp.txt', 'w') as mp:
        for i in l:
            mp.write("name" + ':' + i["name"] + '\t'+"age" + ':' + i["age"] + '\t'+"tell" + ':' + i["tell"] + '\n')
    if sc==1:
        os.remove('./users/' + user.yhmyz)
def main():
    global l
    dqwj()
    while True:
        caidan()    #进入菜单函数
        n = input("请输入您选择的序号数字：")
        if n == "1":    #添加名片函数
            tjmp()
        elif n == "2":  #删除名片函数
            scmp()
        elif n == "3":  #修改名片函数
            xgmp()
        elif n == "4":  #查询名片函数
            cxmp()
        elif n == "5":  #获取所有名片信息函数
            hqsympxx()
        elif n == "6":  #保存并读取
            wdic()
            l=[]
            dqwj()
            print("保存并读取——————成功！")
        elif n == "7":  #退出系统
            user.ycxt()
            wdic()
            break
        else:
            print("输入有误！")
def main2():
    global l
    dqwj()
    while True:
        caidan()
        n = input("请输入您选择的序号数字：")
        if n == "1":
            print("您没有此权限,请联系管理员majiaozhen！")
        elif n == "2":  #只允许删除自己的名片
            scmp2()
        elif n == "3":  #只允许修改自己的名片
            xgmp2()
        elif n == "4":  #只允许查询自己的名片信息
            cxmp2()
        elif n == "5":
            print("您没有此权限,请联系管理员majiaozhen！")
        elif n == "6":  #保存并读取信息，也就是更新一下
            wdic()
            l=[]
            dqwj()
            print("保存并读取——————成功！")
        elif n == "7":
            user.ycxt()
            wdic()
            break
        else:
            print("输入有误！")
l = []   #用来存储员工信息

if __name__ == '__main__':
    sc = 0
    user.main()
    if user.yanzheng==1:
        main()
    elif user.yanzheng==2:
        main2()
    else:
        print("请重新登陆")

