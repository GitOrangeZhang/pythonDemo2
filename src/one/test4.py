userName = 'ChengZhang';
password = '123';
#输入用户名
userNameInput = input("请输入用户名：")
#输入密码
passwordInput = input("请输入密码：")
#登录结果
if userNameInput==userName and passwordInput==password:
    print("登录成功！！！")
else:
    print("登录失败！\r\n密码或用户名不正确！")