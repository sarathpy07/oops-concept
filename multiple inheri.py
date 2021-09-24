# 2 parent class and one child class
class father:
    def parent(self):
        print("i am a family king")
class mother:
    def parent2(self):
        print("i am a family queen")
class son(father,mother):
    def child(self):
        print("i am son of parents")
obj=son()
obj.parent()
obj.parent2()
obj.child()