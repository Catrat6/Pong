from turtle import Turtle

def load_high_score():
    with open("high_score.txt", 'r') as file:
        return int(file.read())

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.p_one_score = 0
        self.p_two_score = 0
        self.penup()
        self.color('green')
        self.goto(0, 240)
        self.hideturtle()
        self.write(f"Player One: {self.p_one_score}  Player Two: {self.p_two_score}", False, "center", ("Arial", 13, "normal"))

    def return_score(self):
        a = self.p_one_score
        b = self.p_two_score

        return a, b

    def player_score(self, left_or_right):
        player = left_or_right
        if player == "right":
            self.clear()
            self.p_one_score += 1
            self.write(f"Player One: {self.p_one_score}  Player Two: {self.p_two_score}", False, "center", ("Arial", 13, "normal"))
        elif player == "left":
            self.clear()
            self.p_two_score += 1
            self.write(f"Player One: {self.p_one_score}  Player Two: {self.p_two_score}", False, "center", ("Arial", 13, "normal"))

    def game_over(self, play_to):
        if self.p_one_score == play_to or self.p_two_score == play_to:
            a_list = [self.p_one_score, self.p_two_score]
            winner = max(a_list)
            if winner == self.p_one_score:
                winner_name = "Player One"
            elif winner == self.p_two_score:
                winner_name = "Player Two"
            self.clear()
            self.write(f"Game over! {winner_name} won the game with a score of {winner}", False, "center", ("Arial", 15, "normal"))



class HighScore(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("Green")
        self.goto(250, -250)
        self.high_score = load_high_score()
        self.write(f"High Score: {self.high_score}", False, "center", ("Arial", 10, "normal"))

    def refresh_high_score(self):
        self.clear()
        self.write(f"High Score: {self.high_score}", False, "center", ("Arial", 10, "normal"))

    def new_high_score(self, score_a, score_b):
        if score_a > self.high_score or score_b > self.high_score:
            a = [score_a, score_b]
            a = max(a)
            self.high_score = a
            with open("high_score.txt", "w") as file:
                file.write(str(a))
