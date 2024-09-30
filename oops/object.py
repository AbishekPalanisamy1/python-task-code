class Abi:
    def __init__(self,name,age) -> None:
       self.name=name
       self.age=age

    def ak(self):
        print(self.name)
        print(self.age)
       

obj=Abi("Abishek",22)
obj()