from turtle import Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")

#adds game loop that keeps the program running, refreshes the screen.
game_is_on = True
while game_is_on:
    screen.update()  # Updates the screen

screen.exitonclick()