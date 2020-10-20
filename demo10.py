import turtle

# 五角星
screen = turtle.getscreen()

turtle.color("red", "yellow")
turtle.begin_fill()
for _ in range(5):
    turtle.fd(150)
    turtle.right(144)
turtle.end_fill()
turtle.mainloop()
