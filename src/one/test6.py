#while练习
#打印1-10之间的偶数
# i=1
# while i<=10:
#     if i%2==0:
#         print(i)
#     # i+=1 等价于 i=i+1
#     i += 1


#计算1-100之和
i=1
sum_i=0
while i<=100:
    sum_i = sum_i + i
    i+=1

print('1到100的和为%d'%sum_i)