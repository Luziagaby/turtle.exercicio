import turtle
lu = turtle.Turtle()
lu.shape("turtle")
lu.pensize(3)

for i in range(6):
    lu.forward(100)
    lu.left(60)

turtle.exitonclick()