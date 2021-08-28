"""
刚果共和国国旗
国旗呈长方形，长与宽之比为3∶2。
旗面由绿、黄、红三色构成，左上方为绿色，右下方为红色，一条黄色宽带从左下角斜贯至右上角。
绿色象征森林资源及对未来的希望；黄色象征丰富的资源和无尽的财富，也代表诚实、宽容和自尊；红色代表热情和刚果人民为非洲的自由和独立洒在这片光荣的土地上的热血。
"""

import turtle
import math

w,h = 900,600 #宽、高
item = w / 3 

turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)

#绿
t.pencolor("#009543")
t.fillcolor("#009543")
t.penup()
t.goto(-w / 2,-h/2)
t.pendown()
t.begin_fill()
t.left(90)
t.fd(h)
t.right(90)
t.fd(item*2)
t.end_fill()


#红
t.pencolor("#dc251e")
t.fillcolor("#dc251e")
t.penup()
t.goto(-item/2,-h/2)
t.pendown()
t.begin_fill()
t.fd(item*2)
t.left(90)
t.fd(h)
t.end_fill()


#黄
c = math.sqrt(math.pow(h ,2)+ math.pow(w/3*2,2))

t.pencolor("#fbdf4b")
t.fillcolor("#fbdf4b")
t.begin_fill()
t.left(90)
t.fd(item)
t.left(45)
t.fd(c)
t.left(135)
t.fd(item)
t.left(45)
t.fd(c)
t.end_fill()

t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="刚果共和国国旗.eps") #将图片保存下来

turtle.done()