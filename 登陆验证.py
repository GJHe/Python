#_*_coding:utf-8_*_
#Author：ymxowgk
name_true = "gaojihe"
password_true = "1234"
name = input("Please input your name：")
if name_true == name:
    i = 0
    while i < 3:
        password = input("Please input your password:")
        if password_true == password:
            print("%s 登陆成功!"%name)
            break
        else:
            i += 1
            print("密码错误，请重新输入")
    else:
        print("密码输入错误次数超过3次，账户已被冻结")
else:
    print("请检查用户名是否输入错误")