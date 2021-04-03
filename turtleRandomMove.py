import random
import turtle

turtle.title('거북이가 마음대로 다니기')
turtle.shape()

while True:
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r,g,b))

    angle = random.randrange(0,360)
    dist = random.randrange(1,100)
    turtle.pendown()
    turtle.left(angle)
    turtle.forward(dist)

turtle.done()