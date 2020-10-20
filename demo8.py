import turtle

q = turtle.Pen()
turtle.bgcolor("black")
sides = 7
colors = ["red", "orange", "yellow", "green", "cyan", "blue", "blue", "purple"]
for x in range(100):
    q.pencolor(colors[x % sides])
    q.forward(x * 3 / sides + x)
    q.lf(360 / sides + 1)
    q.width(x * sides / 200)
turtle.done()