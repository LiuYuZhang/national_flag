"""
马里国旗
马里共和国（Republic of Mali），简称马里，是西非的一个内陆国家，首都为巴马科。
马里国旗是一面由绿、黄、红三条直线组成的三色旗，长与宽的比例为3:2。1961年3月1日，被采用为国旗，以取代马里联邦旗帜中间的黑色人形图案。
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

t.pencolor("#14b53a")
t.fillcolor("#14b53a")
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
t.pencolor("#fcd116")
t.fillcolor("#fcd116")
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
t.pencolor("#ce1126")
t.fillcolor("#ce1126")
t.begin_fill()
t.fd(item)
t.right(90)
t.fd(h)
t.right(90)
t.fd(item)
t.end_fill()

t.hideturtle()

turtle.done()

