"""
索马里国旗

"""

import turtle
from typing import ItemsView

w = 900
h = 600

turtle.screensize(w,h,"white")
turtle.setup(w,h)

#绿
t = turtle.Turtle()
t.pensize(1)
t.speed(10)

t.pencolor("#4189dd")
t.fillcolor("#4189dd")
t.penup()
t.goto(-w/2,0)
t.pendown()
t.begin_fill()
t.left(90)
t.forward(h/2)
t.right(90)
t.fd(w)
t.right(90)
t.fd(h)
t.right(90)
t.fd(w)
t.end_fill()



#星
t.right(180)
t.penup()
t.goto(-80,40)
t.pendown()
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
t.begin_fill() #填充颜色开始
for _ in range(5):
   t.forward(160)
   t.right(144)
t.end_fill() #填充图形颜色前调用

t.hideturtle()


ts = t.getscreen()
ts.getcanvas().postscript(file="索马里国旗.eps") #将图片保存下来

turtle.done()

