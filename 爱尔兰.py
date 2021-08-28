"""
爱尔兰国旗
爱尔兰共和国（Republic of Ireland），简称“爱尔兰”（Ireland），是一个西欧的议会共和制国家。爱尔兰国旗呈横长方形，长与宽之比为2:1。
从左至右由绿、白、橙三个平行相等的竖长方形组成。绿色代表信仰天主教的爱尔兰人，也象征爱尔兰的绿色宝岛；
橙色代表新教及其信徒，这一颜色还取意于奥伦治·拿骚宫的色彩，也表示尊贵和财富；白色象征天主教徒和新教派教徒之间永久休战、团结友爱，还象征对光明、自由、民主与和平的追求。
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

t.pencolor("#169b62")
t.fillcolor("#169b62")
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

#橙
t.pencolor("#ff883e")
t.fillcolor("#ff883e")
t.begin_fill()
t.fd(item)
t.right(90)
t.fd(h)
t.right(90)
t.fd(item)
t.end_fill()

t.hideturtle()

turtle.done()

