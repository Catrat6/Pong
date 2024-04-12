import random
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('white')
        self.x_move = 10
        self.y_move = 10


    def roll_top_right(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)




