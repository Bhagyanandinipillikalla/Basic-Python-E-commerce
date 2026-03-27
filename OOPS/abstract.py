from abc import abstractmethod,ABC
class Developer(ABC):
    # def debug(self):
    #     print("Abstract")
    @abstractmethod
    def code(self):
        print("Incomplete method")
d1=Developer()
d1.debug()   
d1.code()         