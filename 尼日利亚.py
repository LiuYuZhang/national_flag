"""
尼日利亚国旗
日利亚联邦共和国（Federal Republic of Nigeria），简称尼日利亚，处于西非东南部的国家，非洲几内亚湾西岸的顶点，首都阿布贾。
尼日利亚国旗呈横长方形，长与宽之比为2:1。自左至右由绿，白，绿三个相等的垂直长方形组成。绿色象征农业，白色象征和平与统一。
1959年尼日利亚全国国旗设计比赛中获选，此国旗由一名学生设计。1960年10月1日独立，并采用。
"""

import turtle
from typing import ItemsView

w = 900
h = 450
item = w / 3

turtle.screensize(w,h,"white")
turtle.setup(w,h)

#绿
t = turtle.Turtle()
t.pensize(1)
t.speed(10)

t.pencolor("#008751")
t.fillcolor("#008751")
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
t.pencolor("#008751")
t.fillcolor("#008751")
t.begin_fill()
t.fd(item)
t.right(90)
t.fd(h)
t.right(90)
t.fd(item)
t.end_fill()

t.hideturtle()

turtle.done()

