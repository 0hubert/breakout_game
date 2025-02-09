from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

# create paddle
paddle = Paddle((0, -250))
# create ball
ball = Ball()
# create bricks
colors = ["purple","blue","orange","green","yellow"]
bricks = []
for row in range(5):
    y_pos = 150 - (row * 30)
    for col in range(8):
        x_pos = -350 + (col * 100)
        brick = Brick((x_pos,y_pos), colors[row])
        bricks.append(brick)

# setup keyboard controls

# game loop
    #detect collision with walls
    #detect collision with paddle
    #detect collision with bricks
    #detect paddle miss

screen.exitonclick()