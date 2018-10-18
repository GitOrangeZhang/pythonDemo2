num = 100

def test():
    global num
    num = 200
    print(num)

def test1():
    print(num)

test()
test1()