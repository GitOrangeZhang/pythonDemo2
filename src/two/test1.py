#初始化方法
class kid:
    def __init__(self,newName,newGender,newAge):
        self.name = newName
        self.gender = newGender
        self.age = newAge

    def selfIntroduction(self):
        print('我的名字叫：'+self.name+'，我是个'+self.gender+'孩儿，我今天'+self.age+'天了。')

thisKid = kid('张袁嘉泽','男','50')
thisKid.selfIntroduction()