from abc import ABC,abstractmethod


class Tv(ABC):
    @abstractmethod
    def channel(self):
        pass
class Pogo(Tv):
    def channel(self):
        print("Pogo")
class Cn(Tv):
    def channel(self):
        print("cn")

def watch(tv):
    return watch

obj1=Pogo()
obj2=Cn()

# print(obj1.channel())
# print(obj2.channel())

obj1.channel()