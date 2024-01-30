from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.show_score()

    #Detect collision with food
    if snake.all_segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()
        scoreboard.show_score()

    #Detect collison with wall
    if snake.all_segments[0].xcor() > 280 or snake.all_segments[0].xcor() < -280 or snake.all_segments[0].ycor() > 280 or snake.all_segments[0].ycor() < -280:
        scoreboard.reset()
        # snake.reset()
        scoreboard.game_over()
        game_is_on = False

    #Detect collision with tail
    for segment in snake.all_segments[1:]:
        if snake.all_segments[0].distance(segment) < 10:
            scoreboard.reset()
            # snake.reset()
            scoreboard.game_over()
            game_is_on = False
























screen.exitonclick()