class animal:
    def __init__(self, name):
        self.name = name
        print("Animal constructor called")

class bird(animal):
    def __init__(self, name , number):
        super().__init__(name)
        self.number =number
        print("i am here")

my_bird = bird("gau" , 10)

print(my_bird.name)




        



