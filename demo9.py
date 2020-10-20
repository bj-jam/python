import turtle

turtle = turtle.Turtle()
screen = turtle.getscreen()

turtle.color('red', 'yellow')
turtle.begin_fill()
# turtle.hideturtle()
for i in range(1):
    turtle.forward(200)
    turtle.left(170)
turtle.end_fill()
screen.mainloop()
