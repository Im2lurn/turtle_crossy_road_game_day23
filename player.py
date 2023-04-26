from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.left(90)
        self.penup()
        self.color("green")
        self.shape("turtle")
        self.go_to_start()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def successful_crossing(self):
        if self.ycor() > 280:
            return True
        else:
            return False
