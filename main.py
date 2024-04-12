import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('Pong')
screen.tracer(0)

paddle_one = Paddle(350, 0)
paddle_two = Paddle(-350, 0)
ball = Ball()

screen.listen()
screen.onkeypress(paddle_one.move_up, "Up")
screen.onkeypress(paddle_one.move_down, "Down")
screen.onkeypress(paddle_two.move_up, "w")
screen.onkeypress(paddle_two.move_down, "s")

game_state = True

while game_state:
    screen.update()
    time.sleep(0.08)
    ball.roll_top_right()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_one) < 60 and ball.xcor() > 340 or ball.distance(paddle_two) < 60 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 370 or ball.xcor() < -370:



screen.exitonclick()