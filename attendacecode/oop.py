'''class car():
    x="ali"
a=car()
print(a.x)
# use init function
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Ali", 20)
print(s1.name)  
print(s1.age)  ''' 

class car():
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
        pass
car1=car("civic","red")
car2=car("toyota","white")

print(car1.brand,car1.color)
print(car2.brand,car2.color)







