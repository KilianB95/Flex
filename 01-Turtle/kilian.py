import turtle

turtle.speed(0)
turtle.bgcolor("black")
turtle.pencolor("red")
turtle.fillcolor("blue")
turtle.begin_fill()

for x in range(36):
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(250)
    turtle.left(5)

turtle.end_fill()
turtle.done()
