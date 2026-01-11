from turtle import Turtle
CRAB_GIF_FILES = [f"crab_{i}.gif" for i in range(6)]
CRAB_SIZE = 44

class Crab(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.pu()
        self.shape(CRAB_GIF_FILES[0])
        self.goto(x, y)

        self.size = CRAB_SIZE

    def change_shape(self, filename):
        self.shape(filename)
    
    def move_side(self, movement_length):
        self.goto(self.xcor() + movement_length, self.ycor())
    
    def move_down(self, movement_length):
        self.goto(self.xcor(), self.ycor() - movement_length)
