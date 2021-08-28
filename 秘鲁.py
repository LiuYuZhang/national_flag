"""
秘鲁国旗
秘鲁国旗，由三条垂直的红、白、红纵条组成。由何塞·德·圣马丁设计。长方形，长宽之比为3：2。
红色象征胜利，也表示人民对烈士的怀念。旗面自左至右由红白红三个竖长方形相连组成。
白色长方形正中绘有国徽图案。1825年启用，6月7日为国旗日。
"""

import turtle
from typing import ItemsView

w = 900
h = 600
item = w / 3

turtle.screensize(w,h,"white")
turtle.setup(w,h)

#绿
t = turtle.Turtle()
t.pensize(1)
t.speed(10)

t.pencolor("#d91023")
t.fillcolor("#d91023")
t.penup()
t.goto(-item/2,0)
t.pendown()
t.begin_fill()
t.left(90)
t.forward(h//2)
t.left(90)
t.fd(item)
t.left(90)
t.fd(h)
t.left(90)
t.fd(item)
t.end_fill()

#白
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
t.begin_fill()
t.forward(item)
t.left(90)
t.fd(h)
t.left(90)
t.fd(item)
t.left(90)
t.end_fill()
t.right(270)
t.forward(item)

#绿
t.pencolor("#d91023")
t.fillcolor("#d91023")
t.begin_fill()
t.fd(item)
t.right(90)
t.fd(h)
t.right(90)
t.fd(item)
t.end_fill()

t.hideturtle()

turtle.done()

ts = t.getscreen()
ts.getcanvas().postscript(file="秘鲁国旗.eps") #将图片保存下来

