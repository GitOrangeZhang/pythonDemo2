#学生管理系统

#定义一个学生列表
stuInfos = []

while True:
    print('*'*10+'欢迎进入学生管理系统 v3.15'+'*'*10)
    print('1.新增学生信息')
    print('2.删除学生信息')
    print('3.修改学生信息')
    print('4.查看学生信息')
    print('0.退出系统')
    print('*'*51)
    flag = input('请输入选项：')
    if flag=='1':
        #获取键入学生信息
        stuName = input('请输入要新增的学生姓名：')
        stuGender = input('请输入要新增的学生性别：')
        stuAge = input('请输入要新增的学生年龄：')
        #添加学生信息
        stuInfo = {}
        stuInfo['name'] = stuName
        stuInfo['gender'] = stuGender
        stuInfo['age'] = stuAge
        stuInfos.append(stuInfo)
    elif flag=='2':
        stuNum = input('请输入要删除的学生编号：')

    elif flag=='3':
        stuNum = input('请输入要修改的学生编号：')

    elif flag=='4':
        #stuNum = input('请输入要查看的学生编号（all/num）：')
        print('学生信息如下：')
        print('序号\t姓名\t性别\t年龄')
        i = 1
        for tempInfo in stuInfos:
            print('%d\t\t%s\t%s\t%s'%(i,tempInfo['name'],tempInfo['gender'],tempInfo['age']))
            i+=1
    elif flag=='0':
        print('谢谢使用！')
        break
    else:
        print('请输入正确选项！')