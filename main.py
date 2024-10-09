from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setup the game window
screen = Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0) # Turn off automatic screen updates (manual control)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for keyboard inputs to control the snake
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update() # Refresh the screen manually
    time.sleep(0.1) # Control game speed
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh() # Move food to a new random location
        snake.extend() # Add a new segment to the snake
        scoreboard.increase_score() # Update the score

    #Detect collision with wall
    if snake.head.xcor() > 280  or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False # End game
        scoreboard.game_over() # Display "Game Over" message

    # Detect collision with the snake's own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False # End game
            scoreboard.game_over() # Display "Game Over" message

screen.exitonclick()