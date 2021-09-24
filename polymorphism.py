class redmi:
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def show(self):
        print(f"my mbile is {self.name} and model is {self.model}")
    def storoge(self):
        print(f"it have 64 gp internal storoge")
class samsung:
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def show(self):
        print(f"my mbile is {self.name} and model is {self.model}")
    def storoge(self):
        print(f"it have 128 gp internal storoge")
obj1=redmi("redmi","not5pro")
obj2=samsung("samsung","m20")
obj1.show()
obj1.storoge()

print("==========================================")
obj2.show()
obj2.storoge()
