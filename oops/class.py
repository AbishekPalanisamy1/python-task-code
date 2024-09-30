# class Abishek:

#     name="Abishek"
#     age=23
# print(getattr(Abishek,'name'))
# print(getattr(Abishek,'age'))

# setattr(Abishek,'gender','male')
# print(getattr(Abishek,'gender'))

# class Abishek:
#     def __init__(self,name,age) -> None:
#         self.name=name
#         self.age=age
#         print("Heyy")

#     def print(self):
#         print(self.name)
#     @staticmethod
#     def wel():
#         print("hellooo")
# obj=Abishek("Abii",22)
# obj.print()
# obj.wel()





# class Animal():
#     def sound(self,*args):
#         add=0
#         for i in args:
           
#             add+=i
#         print( add)
    

# add=Animal()
# add.sound(1,2,3,4,5,6)


# class Animal:
#     def sound(self):
#         pass
# class Dog(Animal):
#     def sound(self):
#         return "Bark"
# class Cat(Animal):
#     def sound(self):
#         return "Meoww"
# class Cow(Animal):
#     def sound(self):
#         return "Meaaaaa"

# def animal_sound(Animal):
#     return Animal.sound()

# dog=Dog()
# cat = Cat()
# cow = Cow()
# print(animal_sound(dog))
# print(animal_sound(cat))
# print(animal_sound(cow))



# class Animal:
#     def __init__(self):
#         self._abi="public"
#     def abii(self):
#         print("Abishek")
# obj=Animal()
# print(obj._abi)
# print(obj.abii())




class Animal:
    def __init__(self):
        print("Abii")
    def abii(self):
        a='Abishek'
        print(a)
obj=Animal()
obj.abii()