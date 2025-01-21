import turtle
lu = turtle.Turtle()
lu.speed(1)
lu.shape("turtle")
lu.pensize(3)

for i in range(6):  
    for i in range(6):  
        lu.forward(50) 
        lu.left(60)    
    lu.left(60)           


turtle.exitonclick()  
    