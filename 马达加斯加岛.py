"""
马达加斯加岛国旗
马达加斯加共和国（The Republic of Madagascar），简称马达加斯加，是位于印度洋西部的非洲岛国，隔莫桑比克海峡与非洲大陆相望。
马达加斯加岛全岛由火山岩构成，作为非洲第一、世界第四大的岛屿，马达加斯加岛旅游资源丰富，首都塔那那利佛。马达加斯加国旗呈长方形，长宽之比为3：2。
靠旗杆一侧为白色竖长方形，旗面右侧为上红下绿两个横长方形，三个长方形面积相等。白色象征纯洁，红色象征主权，绿色象征希望。
"""

import turtle

w = 900
h = 600
item = w / 15 *6
item2 = w / 15 *9

turtle.screensize(w,h,"white")
turtle.setup(width=w,height=h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)
#t.hideturtle()


#白
t.penup()
t.goto(-w /2  ,0)
t.pendown()
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
t.begin_fill()
t.left(90)
t.forward(h/2)
t.right(90)
t.fd(item)
t.right(90)
t.fd(h)
t.right(90)
t.fd(item)
t.end_fill()


#红
t.right(180)
t.pencolor("#fc3d32")
t.fillcolor("#fc3d32")
t.begin_fill()
t.forward(w)
t.left(90)
t.forward(h / 2)
t.left(90)
t.forward(item2)
t.left(90)
t.forward(h/2)
t.end_fill()


#绿
t.right(180)
t.forward(h/2)
t.pencolor("#007e3a")
t.fillcolor("#007e3a")
t.begin_fill()
t.forward(h/2)
t.right(90)
t.forward(item2)
t.right(90)
t.forward(h /2)
t.end_fill()

ts = t.getscreen()
ts.getcanvas().postscript(file="马达加斯加岛国旗.eps") #将图片保存下来

turtle.done()
