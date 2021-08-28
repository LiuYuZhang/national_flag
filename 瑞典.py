"""
瑞典国旗
瑞典国旗，是瑞典国的国旗，国旗的形状是长方形；国旗的长宽之比为5:8，瑞典的国旗为蓝地黄十字旗，称之为蓝旗。
"""

import turtle

w = 800
h = 500
item = 100

turtle.screensize(w,h,"white")
turtle.setup(w,h)
t = turtle.Turtle()
t.speed(10)
t.pensize(1)
t.hideturtle()


#底色框
t.pencolor("#015293")
t.fillcolor("#015293")
t.penup()
t.goto(-w/2,-h / 2)
t.pendown()
t.begin_fill()
t.forward(w)
t.left(90)
t.forward(h)
t.left(90)
t.forward(w)
t.end_fill()

#横向黄块
t.penup()
t.pencolor("#fecb00")
t.fillcolor("#fecb00")
t.goto(-w/2,-item/2)
t.pendown()
t.right(180)
t.begin_fill()
t.forward(w)
t.left(90)
t.forward(item)
t.left(90)
t.forward(w)
t.end_fill()


#纵向黄
t.penup()
t.goto(-item/2+30,h/2)
t.pendown()
t.begin_fill()
t.forward(item)
t.left(90)
t.forward(h)
t.left(90)
t.forward(item)
t.left(90)
t.end_fill()

ts = t.getscreen()
ts.getcanvas().postscript(file="瑞典国旗.eps") #将图片保存下来

turtle.done()