import turtle
lu = turtle.Turtle()

def desenhe_uma_flor():
    for _ in range(6):  
        for _ in range(8):  
            lu.pensize(2)  
            lu.forward(20)
            lu.right(30)
        lu.right(60) 

lu.penup()
lu.goto(-90, 110)
lu.pendown()

for _ in range(3):  
    desenhe_uma_flor()
    lu.penup()
    lu.forward(150)  
    lu.pendown()

turtle.exitonclick()