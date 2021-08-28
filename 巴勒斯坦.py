"""
巴勒斯坦国旗
巴勒斯坦国旗长方形，长宽之比为2：1。旗面左侧为红色等腰直角三角形，右侧自上而下为黑、白、绿三色等宽横条。
"""

import turtle
import math

w = 900
h = 450
h_m = h/3
c = math.sqrt((math.pow(h / 2,2) + math.pow(h / 2,2))) #三角形边长

turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)

#绿
t.pencolor("#000000")
t.fillcolor("#000000")
t.begin_fill()
t.penup()
t.goto(0,h_m/2)
t.pendown()
t.forward(w/2)
t.left(90)
t.forward(h_m)
t.left(90)
t.forward(w)
t.left(90)
t.forward(h_m)
t.left(90)
t.forward(w/2)
t.end_fill()


#白
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
t.begin_fill()
t.penup()
t.goto(0,-h_m/2)
t.pendown()
t.forward(w/2)
t.left(90)
t.forward(h_m)
t.left(90)
t.forward(w)
t.left(90)
t.forward(h_m)
t.left(90)
t.forward(h / 2)
t.end_fill()

#绿
t.pencolor("#007a3d")
t.fillcolor("#007a3d")
t.begin_fill()
t.penup()
t.goto(0,-h_m-h_m/2)
t.pendown()
t.forward(w/2)
t.left(90)
t.forward(h_m)
t.left(90)
t.forward(w)
t.left(90)
t.forward(h_m)
t.left(90)
t.forward(w/2)
t.end_fill()

#红色等腰直角三角形
t.penup()
t.goto(-w/2,h/2)
t.pendown()
t.pencolor("#ce1127")
t.fillcolor("#ce1127")
t.begin_fill()
t.right(45)
t.fd(c)
t.right(90)
t.fd(c)
t.end_fill()

t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="巴勒斯坦国旗.eps") #将图片保存下来

turtle.done()