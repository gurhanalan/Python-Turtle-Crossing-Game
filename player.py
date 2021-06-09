STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.start_count = 0

    def go_up(self):
        self.forward(MOVE_DISTANCE)
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.start_count += 1

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y