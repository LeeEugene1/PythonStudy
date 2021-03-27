import turtle
import random

#기능1. 마우스 좌클릭시 거북이가 클릭한지점까지 랜덤색상으로 선을그리면서 따라오게한다
#기능2. 마우스 우클릭시 거븍이가 클릭한 지점까지 선을 그리지않고 이동만한다
#기능3. 마우스 가운데클릭시 거북이가 임의로 크기를 바꾼다

turtle.shape('turtle')

#변수준비 선두께,거북이크기,rgb
pSize, tSize = 10, 0
r,g,b = 0,0,0

#기능구현
def leftClick(x,y):
    global r,g,b
    #컬러랜덤
    turtle.pencolor((r,g,b))
    #펜을 찍는다
    turtle.pendown()
    #x,y좌표까지 이동한다
    turtle.goto(x,y)

def rightClick(x,y):
    #펜을 든다
    turtle.penup()
    #x,y좌표까지 이동한다
    turtle.goto(x,y)

def middleClick(x,y):
    global r,g,b
    #컬러랜덤
    r = random.random()
    g = random.random()
    b = random.random()

    #거북이 크기랜덤
    tSize = random.randrange(1,10)
    
    #펜크기 랜덤
    pSize = turtle.shapesize(tSize)


turtle.onscreenclick(leftClick,1)
turtle.onscreenclick(rightClick,3)
turtle.onscreenclick(middleClick,2)

turtle.done()