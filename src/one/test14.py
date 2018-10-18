#文件的操作
#coding=utf-8
'''
r = open('test123.txt','r')
str = r.read()
print(str)
'''
#创建一个txt文件
f = open('test321.txt','w')
#写入一句话
f.write('你好呀，这到底是什么字符集呢？')
#文件关闭
f.close()
#只读方式打开这个txt文件
f1 = open('test321.txt','r')
#读
str1 = f1.read()
#打印读出的内容
print(str1)
#文件关闭
f1.close()