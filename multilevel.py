# one base class one or more child class
class mobile:
    def parent(self):
        print('i am a root of our family')
class redmi(mobile):
    def child1(self):
        print("i am child of our family")
class redmi5pro(redmi):
    def child2(self):
        print("i am new model of our family")
obj=redmi5pro()
obj.parent()
obj.child1()
obj.child2()