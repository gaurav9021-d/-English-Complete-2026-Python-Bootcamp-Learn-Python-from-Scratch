#class attribute
# Class Attribute wo variable hota hai jo class ke andar define kiya jata 
# hai aur class ke sabhi objects usko share karte hain.

class student:
    school  = "ABC School" #class attribute
s1 = student()
s2 = student()

print(s1.school)
print(s2.school)

#instance attribute

# Instance Attribute wo variable hota hai jo har 
# object ke liye alag-alag value store karta hai. 

class Student:
    def __init__(self , name , age):
        self.name = name  # instance attribute
        self.age = age

s1 = Student("gaurav" , 19)
s2 = Student("shiva" , 20)

print(s1.name , s1.age)
print(s2.name , s2.age)


# both of think combine

class Student:
    school = "ABC School"  #class Attribute

    def __init__(self, name , age):
        self.name = name #instance attribute
        self.age = age   #instance attribute

s1 = Student("Gaurav" , 21)
s2 = Student("rahul" , 22)

print(s1.name)
print(s1.age)
print(s1.school)

print(s2.name)
print(s2.age)
print(s2.school)
