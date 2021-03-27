import turtle

turtle.shape('turtle')

# default는 거북이가 우측을 바라보고있다 forward는 앞으로, right(90)은 회전
# turtle.forward(200)
# turtle.right(90)

for move in range(0,4):
    turtle.forward(200)
    turtle.right(90)

turtle.done()