"""
乍得国旗
乍得共和国（Republic of Chad），简称“乍得”（或译查德），是非洲中部的一个内陆国家，首都及最大城市为恩贾梅纳。乍得国旗呈长方形，长与宽之比为3:2。
旗面由三个平行相等的竖长方形构成。从左至右依次为蓝、黄、红三色。蓝色象征蓝天、希望和生活，还代表该国的南部；黄色象征阳光，以及该国的北部；红色象征进步、团结和愿为祖国献身的精神。
乍得国旗与罗马尼亚国旗几乎相同。仅蓝色部分略深。
"""

import turtle
from typing import ItemsView

w = 900
h = 600
item = w / 3

turtle.screensize(w,h,"white")
turtle.setup(w,h)

#蓝
t = turtle.Turtle()
t.pensize(1)
t.speed(10)

t.pencolor("#002664")
t.fillcolor("#002664")
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

#黄
t.pencolor("#fecb00")
t.fillcolor("#fecb00")
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

#红
t.pencolor("#c60c30")
t.fillcolor("#c60c30")
t.begin_fill()
t.fd(item)
t.right(90)
t.fd(h)
t.right(90)
t.fd(item)
t.end_fill()

t.hideturtle()



turtle.done()

