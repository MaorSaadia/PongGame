from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from tkinter import *
from tkinter import messagebox
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PongGame")
screen.bgpic("PongBackground.png")
screen.update()
screen.tracer(0)

r_paddle = Paddle((370, 0))
l_paddle = Paddle((-370, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 350 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 385:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle misses:
    if ball.xcor() < -385:
        ball.reset_position()
        scoreboard.r_point()

    if scoreboard.l_score == 7:
        messagebox.showinfo("Game Info", f"Left Player Won!")
        game_is_on = False
    elif scoreboard.r_score == 7:
        messagebox.showinfo("Game Info", f"Right Player Won!")
        game_is_on = False


screen.exitonclick()