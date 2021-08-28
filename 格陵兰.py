"""
格陵兰国旗
陵兰旗是一位格陵兰原住民图厄·基斯当臣 （Thue Christiansen）设计的。在击败一面以北欧十字为基础的设计后，于1985年6月21日启用。
根据设计者的解释，白色横条代表占当地土城面积80%的冰片和冰盖，红色横条代表海洋。红色半圆代表太阳，白色半圆象征冰山。整个画面令另人联想到夕阳西下，太阳的影子投射在海面上。
本旗在格陵兰语被称为 Erfalasorput （我们的旗帜），另外 Aappalaartoq （红旗）可以指本旗或丹麦国旗。
"""

import turtle
import math

w = 900
h = 600
item = h / 2
turtle.screensize(w,h,"white")
turtle.setup(w,h)


t = turtle.Turtle()
t.pensize(1)
t.speed(10)

#白
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
t.begin_fill()
t.forward(w/2)
t.left(90)
t.forward(item)
t.left(90)
t.forward(w)
t.left(90)
t.forward(item)
t.left(90)
t.forward(w/2)
t.end_fill()


#红
t.pencolor("#d00c32")
t.fillcolor("#d00c32")
t.begin_fill()
t.forward(w/2)
t.right(90)
t.forward(item)
t.right(90)
t.forward(w)
t.right(90)
t.forward(item)
t.right(90)
t.forward(w/2)
t.end_fill()

t.left(90)
t.penup()
t.goto(100,0)
t.pendown()
t.begin_fill()
t.circle(h/2 * 0.68 ,180)
t.end_fill()


t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.circle(h/2 * 0.68 ,180)
t.end_fill()

t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="格陵兰国旗.eps") #将图片保存下来

turtle.done()