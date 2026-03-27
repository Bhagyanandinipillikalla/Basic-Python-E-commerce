#Single level inheritance
class Plant:
    def displays(self):
        print("Main Plant")
class Indoor(Plant):
    def display(self):
        print("Less water and sun light")
i1=Indoor()
i2=Plant()
# i1.display()  
# i2.display()              

#Multi level inheritance
class Plants:
    def display(self):
        print("Grow the plants")
class Floweringplant(Plants):
    def flow(self):
        print("Blom the flowers")
class Roseplant(Floweringplant):
    def rose(self):
        print("Roses are RED")        
# r1=Roseplant()
# r1.display()
# r1.flow()
# r1.rose()

#Hierarchical inheritance
class plants:
    def display(self):
        print("Grow the plants")
class Indoorplants(plants): 
    def indoor(self):
        print("Grow me in inside with less water")
class outdoorplants(plants):
    def outdoor(plants):
        print("I need more sunlight and water")
# o1=outdoorplants()
# o1.outdoor()               
# o1.display()

#Multiple  inheritance
class plant:
    def dispaly(self):
        print("Plant Class")
class Indoorplant():
    def grow(self):
        print("Indoor Plant")
class Moneyplant(plant,Indoorplant):
    def climbing(self):
        print("Less water and Maintance")                
# p1=Moneyplant()
# p1.climbing()
# p1.grow()

class car:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def get_name(self):
        return self.name
    @property
    def get_price(self):
        return self.price
c1=car('BMW',24441)
# print(c1.get_name)
# print(c1.get_price)    

class car:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def set_price(self,price):
        self.price=price
    @property
    def get_price(self):
        return self.price
c1=car("bMW",3444)
# c1.set_price(9999999)
# print(c1.get_price)  


class car:
    carname=None
    _price=None
    def __init__(self,carname,price):
        self.carname=carname
        self._price=price
    def  getcarname(self):
        return self.carname 
    def _get_price(self):
        return self._price
c1=car("Thar",39999)
# print(c1.carname)
# print(c1.getcarname())
# print(c1._price)
# print(c1._get_price())    



class car:
    __carname=None
    __price=None
    def __init__(self,carname,price):
        self.__carname=carname
        self.__price=price
    def getcarname(self):
        return self.__carname
    def _get_price(self):
        return self.__price
# c1=car("Honda",88888)
# print(c1.getcarname())   
# print(c1._get_price()) 


class student:
    def __init__(self,name,grade):
        self.name=name
        self.__grade=grade
    def get_grade(self):
        return self.__grade
    def set_grade(self,grade):
        if 0<=grade<=100:
            self.__grade=grade
        else:
            print("Invalid grade")
s1=student("nbv",77)
print(s1.get_grade(),s1.name)
s1.set_grade(99)                
print(s1.get_grade())
