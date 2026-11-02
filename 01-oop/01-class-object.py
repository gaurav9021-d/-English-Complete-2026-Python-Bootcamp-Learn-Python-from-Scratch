class Student:
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


# Create object
student1 = Student()

# Add values after creating the object
student1.name = "Gaurav"
student1.age = 20

# Call method
student1.show_details()






class collage:
    def show_collage_info(self):
        print(self.name)
        print(self.age)

col01 = collage()

col01.name = "Gaurav"
col01.age = 20

col01.show_collage_info()



class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)


student1 = Student("Gaurav", 20)  # Values passed while creating object

student1.show_details()


class student:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def show_details(self):
        print(self.name)
        print(self.age)

student1 = student("Gau", 20)

student1.show_details()

