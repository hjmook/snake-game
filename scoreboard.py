from turtle import Turtle


class Scoreboard(Turtle):
    current_score = 0

    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as high_score:
            self.high_score = int(high_score.read())

    def show_score(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.write(f"Score: {self.current_score} High Score: {self.high_score}", move=False, align="center", font=("arial", 20, "normal"))

    def add_score(self):
        self.clear()
        self.current_score += 1

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open("data.txt", mode="w")as h_score:
                h_score.write(f"{self.high_score}")
        self.current_score = 0
        self.show_score()

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write("Game over", move=False, align="center", font=("arial", 20, "normal"))
