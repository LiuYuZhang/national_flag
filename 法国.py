"""
法国国旗
法兰西共和国（French Republic，France），简称“法国”，是一个本土位于西欧的半总统共和制国家，海外领土包括南美洲和南太平洋的一些地区。
法国国旗三色旗是法国大革命时巴黎国民自卫队队旗。白色代表国王，蓝、红色代表巴黎市民，是王室和巴黎资产阶级联盟的象征。
今天的法国人民也认为，三色旗上的蓝色是自由的象征，白色是平等的象征，而红色代表了博爱，正如法国人民“自由、平等、博爱”（法语："Liberté, égalité, fraternité"）的宣言。
1946年宪法确认其为国旗。三色带的宽度比为37:30:33。
"""

import turtle
from typing import ItemsView

w = 900
h = 600
item1 = w * 0.37
item2 = w * 0.30
item3 = w * 0.33

turtle.screensize(w,h,"white")
turtle.setup(w,h)

#蓝
t = turtle.Turtle()
t.pensize(1)
t.speed(10)

t.pencolor("#002496")
t.fillcolor("#002496")
t.penup()
t.goto(-item1/2,0)
t.pendown()
t.begin_fill()
t.left(90)
t.forward(h//2)
t.left(90)
t.fd(item1)
t.left(90)
t.fd(h)
t.left(90)
t.fd(item1)
t.end_fill()

#白
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
t.begin_fill()
t.forward(item2)
t.left(90)
t.fd(h)
t.left(90)
t.fd(item2)
t.left(90)
t.end_fill()
t.right(270)
t.forward(item2)

#红
t.pencolor("#ed2839")
t.fillcolor("#ed2839")
t.begin_fill()
t.fd(item3)
t.right(90)
t.fd(h)
t.right(90)
t.fd(item3)
t.end_fill()

t.hideturtle()

turtle.done()

