import turtle
lu = turtle.Turtle()

def desenhe_triangulo():
    for _ in range(3):
        lu.forward(50)
        lu.left(120)

def desenhe_quadrado():
    for _ in range(4):
        lu.forward(50)
        lu.left(90)

def desenhe_octogono():
    for _ in range(8):
        lu.forward(20)
        lu.left(45)

def pule(pixels):
    lu.penup()
    lu.forward(pixels)
    lu.pendown()

for _ in range(3):  
    desenhe_triangulo()
    pule(75)  

lu.left(90) 

for _ in range(3):  
    desenhe_quadrado()
    pule(75) 

lu.left(90) 

for _ in range(3):  
    desenhe_octogono()
    pule(75)  

    lu.left(90)
turtle.exitonclick()