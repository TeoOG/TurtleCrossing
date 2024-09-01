from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "cyan", "pink"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LEFT_HEADING = 180


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()

    def create_car(self):
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(LEFT_HEADING)
        self.goto(random.randint(200, 15000), random.randint(-250, 250))
        # self.increment_distance += 5

    def move(self):
        # self.forward(MOVE_INCREMENT)
        self.forward(STARTING_MOVE_DISTANCE)



