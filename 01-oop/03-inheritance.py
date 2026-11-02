class employee:
    def __init__(self,name ,id):
        self.name = name
        self.id = id

    def showdetails(self):
        print(f"name is {self.name} or {self.id}")

class program(employee):
    def uselanguage(self):
        print("we use python programing language")

e1 = employee("gaurav" , 12)
e2 = program("jay" , 22)
e1.showdetails()
e2.uselanguage()



class Animal:  # Parent class (superclass)
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Generic animal sound")

class Dog(Animal):  # Dog inherits from Animal (Dog is a subclass of Animal)
    def speak(self):  # We *override* the speak method (more on this later)
        print("Woof!")

class Cat(Animal):  # Cat also inherits from Animal
    def speak(self):
        print("Meow!")

# Create objects:
my_dog = Dog("Rover")
my_cat = Cat("Fluffy")

# They both have a 'name' attribute (inherited from Animal):
print(my_dog.name)  # Output: Rover
print(my_cat.name)  # Output: Fluffy

# They both have a 'speak' method, but it behaves differently:
my_dog.speak()  # Output: Woof!
my_cat.speak()  # Output: Meow!

# Inheritance OOP (Object-Oriented Programming) ka ek concept hai jisme
#  ek class dusri class ki properties (variables) aur methods (functions)
#  ko reuse kar sakti hai.
# Simple words me:
# Inheritance ka matlab hai Parent Class ki qualities ko Child
#  Class me inherit (paana) karna.

# ypes of Inheritance (Hinglish)

# Single Inheritance
#  Ek Child Class sirf ek Parent Class se inherit karti hai.

# Multiple Inheritance
#  Ek Child Class ek se jyada Parent Classes se inherit karti hai.

# Multilevel Inheritance
#  Parent → Child → Grandchild wali inheritance chain.

# Hierarchical Inheritance
#  Ek Parent Class se multiple Child Classes inherit karti hain.

# Hybrid Inheritance
#  Do ya do se jyada inheritance types ka combination.