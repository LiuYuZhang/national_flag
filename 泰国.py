"""
泰国国旗
泰王国国旗呈长方形、长与宽之比为3:2。由红、白、蓝（双倍宽）、白和红（位于上下两边）的五个长条组成
"""

import turtle
from typing import ItemsView

width = 900
height = 600
turtle.screensize(width,height,"white")
turtle.setup(width=width,height=height)
item = height / 6

t = turtle.Turtle()
t.pensize(1)
t.speed(10)


#红色
t.penup()
t.goto(0,height/2)
t.pendown()
t.pencolor("#d0020f")
t.fillcolor("#d0020f")
t.left(90)
t.begin_fill()
t.right(90)
t.forward(width/2)
t.right(90)
t.forward(item)
t.right(90)
t.forward(width)
t.right(90)
t.forward(item)
t.right(90)
t.forward(width/2)
t.end_fill()

#白色
t.penup()
t.goto(0,height/2 - item)
t.pendown()
t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.forward(width/2)
t.right(90)
t.forward(item)
t.right(90)
t.forward(width)
t.right(90)
t.forward(item)
t.right(90)
t.end_fill()

# #蓝色
t.pencolor("#000ba1")
t.fillcolor("#000ba1")
t.penup()
t.goto(0,item)
t.pendown()
t.begin_fill()
t.forward(width /2)
t.right(90)
t.forward(item*2)
t.right(90)
t.forward(width)
t.right(90)
t.forward(item*2)
t.right(90)
t.forward(width /2)
t.end_fill()

#白色
t.penup()
t.goto(0, - item)
t.pendown()
t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.forward(width/2)
t.right(90)
t.forward(item)
t.right(90)
t.forward(width)
t.right(90)
t.forward(item)
t.right(90)
t.end_fill()

# #红色
t.penup()
t.goto(0,-height/2)
t.pendown()

t.pencolor("#d0020f")
t.fillcolor("#d0020f")
t.begin_fill()
t.fd(width / 2)
t.left(90)
t.fd(item)
t.left(90)
t.fd(width)
t.left(90)
t.fd(item)
t.left(90)
t.fd(width / 2)
t.end_fill()

t.hideturtle()


ts = t.getscreen()
ts.getcanvas().postscript(file="泰国国旗.eps") #将图片保存下来

turtle.done()
