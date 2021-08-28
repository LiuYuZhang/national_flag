"""
波多黎各国旗
波多黎各旗帜由3条红色和两条白色的色带组成。红色与白色互相交替。左侧为一蓝色三角形，
三角形中心处有一五角星。而1952到1995年间的波多黎各旗帜，虽然图案与现在的旗帜完全相同，但三角形的蓝色更深。
"""

import turtle
import math

w = 900
h = 600
h_m = h/5
c = math.sqrt((math.pow(h / 2,2) + math.pow(w / 2,2))) #根据勾股定理计算三角形边长
print(c)

turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)

#红
t.pencolor("#ee0000")
t.fillcolor("#ee0000")
t.penup()
t.goto(w/2,h/2)
t.pendown()
t.begin_fill()
for i in range(4):
    t.right(90)
    if i % 2 == 0:
        t.fd(h_m)
    else:
        t.fd(w)
t.end_fill()



#白
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
t.penup()
t.home()
t.goto(w/2,h/2 + h_m)
t.pendown()
t.begin_fill()
for i in range(4):
    t.right(90)
    if i % 2 == 0:
        t.fd(h_m)
    else:
        t.fd(w)
t.end_fill()


#红
t.pencolor("#ee0000")
t.fillcolor("#ee0000")
t.penup()
t.home()
t.goto(w/2, h_m /2)
t.pendown()
t.begin_fill()
for i in range(4):
    t.right(90)
    if i % 2 == 0:
        t.fd(h_m)
    else:
        t.fd(w)
t.end_fill()

#白
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
t.penup()
t.home()
t.goto(w/2, - h_m /2)
t.pendown()
t.begin_fill()
for i in range(4):
    t.right(90)
    if i % 2 == 0:
        t.fd(h_m)
    else:
        t.fd(w)
t.end_fill()


#红
t.pencolor("#ee0000")
t.fillcolor("#ee0000")
t.penup()
t.home()
t.goto(w/2, - h_m /2 - h_m)
t.pendown()
t.begin_fill()
for i in range(4):
    t.right(90)
    if i % 2 == 0:
        t.fd(h_m)
    else:
        t.fd(w)
t.end_fill()

#蓝色三角形
t.penup()
t.right(90)
t.goto(-w/2,h/2)
t.pendown()
t.pencolor("#0050ef")
t.fillcolor("#0050ef")
t.begin_fill()
t.fd(h/2)
t.left(90)
t.fd(w/2)
t.end_fill()

t.penup()
t.goto(-w/2,-h /2)
t.pendown()
t.begin_fill()
t.left(90)
t.fd(h/2)
t.right(90)
t.fd(w/2)
t.end_fill()


#星
x = h_m * 1.1
t.pencolor("white")
t.fillcolor("white")
t.penup()
t.home()
t.goto(-360,20)
t.pendown()
t.begin_fill()
for _ in range(5):
   t.forward(x)
   t.right(144)
t.end_fill()

t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="波多黎各国旗.eps") #将图片保存下来

turtle.done()