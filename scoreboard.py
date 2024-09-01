from turtle import Turtle

FONT = ("Courier", 24, "bold")
ALIGNMENT_SCORE = "left"
ALIGNMENT_GAME_OVER = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.create_scoreboard()

    def create_scoreboard(self):
        self.color("black")
        self.penup()
        self.goto(-275, 255)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT_SCORE, font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align=ALIGNMENT_GAME_OVER, font=FONT)
