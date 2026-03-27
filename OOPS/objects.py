class person:
    name="Rani"
    age="22"

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
# p1=person()        
# p1.display()


class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print("My name is",self.name)
        print("My age is",self.age)
s1=student('Vani',21)
s2=student('Geetha',21)
s1.show()            
s2.show()