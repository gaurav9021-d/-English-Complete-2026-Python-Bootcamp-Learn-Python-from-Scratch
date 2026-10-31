class shape:
    def __init__(self , x , y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y

class circle(shape):
    def __init__(self , radius):
        self.radius = radius
        super().__init__(radius , radius)

    def area(self):
        return 3.14 * super().area()
# sq = shape(3,5)
# print(sq.area())

c1 = circle(2)
print(c1.area())