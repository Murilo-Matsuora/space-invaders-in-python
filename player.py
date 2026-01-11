from turtle import Turtle
PLAYER_SPEED = 10
SCREEN_HEIGHT = 800

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.seth(90)
        self.color("white")
        self.shapesize(1.5, 1.5)
        self.goto(0, -SCREEN_HEIGHT/2 + 50)

        self.score = 0

    def move_player_left(self):
        self.goto(self.xcor() - PLAYER_SPEED, self.ycor())

    def move_player_right(self):
        self.goto(self.xcor() + PLAYER_SPEED, self.ycor())
