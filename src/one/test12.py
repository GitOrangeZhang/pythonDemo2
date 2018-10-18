#匿名函数
#lambda 定义一个匿名函数，后面跟参数+冒号+表达式
sum = lambda args1,args2:args1+args2

#print(sum(10,10))


#匿名函数的应用
#对字典中的指定值进行排序
b = [{'xh':1,'age':26},{'xh':2,'age':30},{'xh':3,'age':27},{'xh':4,'age':22},{'xh':5,'age':28}]

#按age排序
#b.sort(key=lambda a:a['age'])
#按xh拍降序
b.sort(key=lambda a:a['xh'],reverse=True)
print(b)


