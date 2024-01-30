from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.all_segments = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            segment = Turtle()
            segment.shape("square")
            segment.color("white")
            segment.penup()
            segment.setposition(x=0 - 20 * i, y=0)
            self.all_segments.append(segment)

    def move(self):
        for seg_num in range(len(self.all_segments) - 1, 0, -1):
            new_x = self.all_segments[seg_num - 1].xcor()
            new_y = self.all_segments[seg_num - 1].ycor()
            self.all_segments[seg_num].goto(new_x, new_y)
        self.all_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.all_segments[0].heading() != DOWN:
            self.all_segments[0].setheading(UP)

    def down(self):
        if self.all_segments[0].heading() != UP:
            self.all_segments[0].setheading(DOWN)

    def left(self):
        if self.all_segments[0].heading() != RIGHT:
            self.all_segments[0].setheading(LEFT)

    def right(self):
        if self.all_segments[0].heading() != LEFT:
            self.all_segments[0].setheading(RIGHT)

    def add_segment(self, position):
            segment = Turtle()
            segment.shape("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.all_segments.append(segment)

    def extend(self):
        self.add_segment(self.all_segments[-1].position())

    def reset(self):
        for seg in self.all_segments:
            seg.goto(1000, 1000)
        self.all_segments.clear()
        self.create_snake()


