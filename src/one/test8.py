#花名册系统

names = []
while True:
    print('=' * 30)
    print('------------欢迎进入花名册管理系统---------------')
    print('1.添加一个名字')
    print('2.删除一个名字')
    print('3.修改一个名字')
    print('4.查询一个名字')
    print('5.查询所有名字')
    print('0.退出系统')
    print('=' * 30)

    #获取输入的选择
    inputOption = input('请选择：\r\n')
    inputName = ''
    #根据选择做出提示
    if inputOption == '1':
        #新增输入的名字
        inputName = input('请输入您要添加的名字：\r\n')
        names.append(inputName)
        print('添加成功！')
    elif inputOption == '2':
        #删除输入的名字
        inputName = input('请输入您要删除的名字：\r\n')
        names.remove(inputName)
        print('删除成功！')
    elif inputOption == '3':
        #请输入您要修改的名字
        inputName = input('请输入您要修改的名字：\r\n')
        names.index(inputName)
        print('修改成功！')
    elif inputOption == '4':
        #请输入您要查看的名字
        print('')
    elif inputOption == '5':
        #查看目前花名册中所有的名字
        for name in names:
            print(name)
    elif inputOption == '0':
        #退出系统
        break