#猜拳游戏
#导入随机生成器
import random
#玩家出拳
a = input("老铁，请出拳（石头【0】，剪刀【1】，布【2】）：")
#电脑出拳
b = str(random.randint(0,2))

#打印电脑出的东西
if b=='0':
    print('电脑出的石头')
elif b=='1':
    print('电脑出的剪刀')
else:
    print('电脑出的布')

#判断谁输谁赢
if (a=='0' and b=='1')  or (a=='1' and b=='2') or (a=='2' and b=='0'):
    print('我赢了，电脑傻蛋，电脑输了。')
elif a==b:
    print('哟，平局，来继续干，决战到天亮，谁跑谁孙子。')
else:
    print('我输了？\r\n重来，弄啥呢嘛，电脑作弊...')
