from turtle import Turtle
import time
DURATION = 1

class Explosion(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.pu()
        self.goto(x, y)
        self.shape("explosion.gif")
        self.start_time = time.time()
    
    def end_after_duration(self):
        if time.time() - self.start_time > DURATION:
            self.hideturtle()
            return True
        return False
