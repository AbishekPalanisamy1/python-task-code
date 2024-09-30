class company():
    def __init__(self,name):
        self.__name=name

    
    def main(self):
        print(self.__name)
       
    
    # def com(self):
    #     print(self.__name)

    # def set_name(self,new_name):
    #     self.__name=new_name

    # def main(self):
    #     print(self.__name)


c=company("abii")
# print(c.com())
# c.set_name("abishek")
# print(c.com())
print(c.__name)

