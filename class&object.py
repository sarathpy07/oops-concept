#class
class mobile:
    def __init__(self,name,model,price):
       self.name=name
       self.model=model
       self.price=price

    def display(self):
       #print("my mobile name is "+ self.name + " and model is "  +self.model+" and price is "+str(self.price))
       return f"my mobile is {self.name}  and its model is {self.model} and {self.price} its price"

    def storoge(self,storoge):
        return f"{self.name} has a {storoge} Gp storoge to use"

#object creation

obj=mobile("redmi","Note5pro",10000)
print(obj.display())
print(obj.storoge(64))
print("================================================")
#multiple obj creation

obj2=mobile("samsung","m30",12000)
print(obj2.display())
print(obj2.storoge(100))
