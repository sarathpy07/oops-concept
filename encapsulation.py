class mobile:
    def __init__(self):
        self.a="redmi"
        self.__b="samsung"
    def display(self):
        print(self.a,self.__b)
obj=mobile()
obj.display()
print(obj.a)
#print(obj.__b)
#__b is private so do not access out of class shows error