import chardet
import os
path = "D:\BaiduNetdiskDownload\电子书\恐怖灵异\恐怖"    # 所有txt存放的文件夹的路径
files = os.listdir(path)   # 读取所有txt的文件名，包含后缀名
print(files)
print(len(files))
for file in files:    # 循环所有txt
    p = path + "\\" + file   # 拼接各个txt的路径
    f = open(p, 'rb',)  # 打开文件，读取内容，判断编码
    data = f.read()
    f.close()
    txtEncoding = chardet.detect(data).get("encoding")
    cuo = []
    if txtEncoding == "GB2312":   # 经个人实验，发现ANSI编码检测时为GB2312编码，所以以此为判断条件
        print(file)
        with open(p, 'r') as f:  # 读取编码为ANSI编码txt的内容，存放到一个变量里
            content = f.read()
        f.close()

        with open(p, 'w', encoding="utf-8") as f:  # 把读取的内容，存入原txt中，替换原内容
            f.write(content)
        f.close()
    else:
        cuo.append(file)
print("cuo"+cuo)