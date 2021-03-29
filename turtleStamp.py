import turtle
import random

tSize = 0
r,g,b = 0,0,0
turtle.title('거북이스템프')
turtle.shape('turtle')

def screenClick(x,y):
    global r,g,b,tSize
    r = random.random()
    g = random.random()
    b = random.random()
    tSize = random.randrange(1,10)

    #클릭시 펜이 클릭한좌표로 이동한다
    turtle.penup()
    turtle.goto(x,y)


    #거북이가 회전한다
    turtle.right(45)

    #팬이내려간다
    # turtle.pendown()

    #거북이를 생성한다(랜덤컬러, 랜덤거북이사이즈로)
    turtle.shapesize(tSize)
    # print(tSize)
    turtle.color((r,g,b))
    turtle.stamp()

    #팬이올라간다
    turtle.penup()

turtle.onscreenclick(screenClick,1)

turtle.done()