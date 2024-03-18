from abc import ABC,abstractmethod
#abc = Abstract Base class
#ABC = Absalute Base class

class calculator(ABC):
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def mul(self):
        pass



if __name__ == "__main__":
    