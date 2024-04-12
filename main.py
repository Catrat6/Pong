import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import ScoreBoard, HighScore


screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('Pong')
screen.tracer(0)


player_one_right = Paddle(350, 0)
player_two_left = Paddle(-350, 0)
ball = Ball()
score = ScoreBoard()
high_score = HighScore()

screen.listen()
screen.onkeypress(player_one_right.move_up, "Up")
screen.onkeypress(player_one_right.move_down, "Down")
screen.onkeypress(player_two_left.move_up, "w")
screen.onkeypress(player_two_left.move_down, "s")

game_state = True

print('''
Welcome to Pong!
Select Game Length and Speed in the Terminal first.
1. You will have 5 second to click the game window before the game starts
    The window must be selected for controls to work.

Player One Controls: Up: "up arrow"  Down: "Down arrow"

Player Two Controls: Up: "W key"     Down: "S key"
''')

play_to = int(input("What number would you like to play to? Put 0 for infinite:\n"))
speed = input("How fast should the ball go? (Slow/Medium/Fast):\n").lower()
if speed in ['slow', 'slo', 's']:
    speed = 0.1
elif speed in ['medium', 'med', 'medi', 'm']:
    speed = 0.06
elif speed in ['fast', 'fas', 'fa', 'f', 'fat']:
    speed = 0.045

time.sleep(5)

while game_state:
    screen.update()
    time.sleep(speed)
    ball.roll_top_right()
    a, b = score.return_score()
    high_score.new_high_score(a, b)
    high_score.refresh_high_score()

    if score.p_one_score == play_to and score.p_one_score != 0 or score.p_two_score == play_to and score.p_two_score != 0:
        score.game_over(play_to)
        break

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(player_one_right) < 60 and ball.xcor() > 340 or ball.distance(player_two_left) < 60 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 370:
        ball.reset()
        score.player_score("left")

    if ball.xcor() < -370:
        ball.reset()
        score.player_score("right")



screen.exitonclick()