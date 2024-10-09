from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20 # Distance the snake moves in each step
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] # The first segment is the snake's head

    def create_snake(self):
        # Create the initial snake with 3 segments
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        # Create a new segment and add it to the snake
        new_segment = Turtle(shape='square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        # Add a new segment to the snake at the position of the last segment
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Move each segment to the position of the segment in front of it
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Functions to change the snake's direction
    def up(self):
        if self.head.heading() != DOWN:  # Prevents reversing direction
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:  # Prevents reversing direction
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:  # Prevents reversing direction
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:  # Prevents reversing direction
            self.head.setheading(RIGHT)

