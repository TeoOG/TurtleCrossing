from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
TURTLE_HEADING = 90


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.refresh()
        self.setheading(TURTLE_HEADING)

    def move(self):
        get_x_cor = self.xcor()
        get_y_cor = self.ycor()
        self.goto(get_x_cor, get_y_cor + MOVE_DISTANCE)

    def refresh(self):
        self.goto(STARTING_POSITION)
