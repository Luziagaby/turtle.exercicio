import turtle

leo = turtle.Turtle()
leo.shape("turtle")
leo.pensize(3)


for _ in range(12):  
    leo.forward(60)
    leo.left(30)
    leo.forward(60)
    leo.left(150)
    leo.forward(60)
    leo.left(30)
    leo.forward(60)

turtle.exitonclick()