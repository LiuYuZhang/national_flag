"""
圣多美和普林西比民主共和国国旗
圣多美和普林西比国旗呈横长方形，长与宽之比为2：1。由红、绿、黄、黑四色构成。靠旗杆一侧为红色等腰三角形，右侧为三个平行宽条，中间为黄色，上下为绿色，黄色宽条中有两颗黑色五角星。
绿色象征农业，黄色象征可可豆和其他自然资源，红色象征为独立自由而斗争战士的鲜血，两个五角星代表圣多美、普林西比两个大岛，黑色象征黑人。
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
t.pencolor("#12ad2b")
t.fillcolor("#12ad2b")
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


#黄
t.pencolor("#fece00")
t.fillcolor("#fece00")
t.begin_fill()
t.penup()
t.goto(w / 2,-h_m/2)
t.pendown()

t.left(90)
t.forward(h_m)
t.left(90)
t.forward(w)
t.left(90)
t.forward(h_m)
t.left(90)
t.forward(w)
t.end_fill()

#绿
t.pencolor("#12ad2b")
t.fillcolor("#12ad2b")
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
t.pencolor("#d21034")
t.fillcolor("#d21034")
t.begin_fill()
t.right(45)
t.fd(c)
t.right(90)
t.fd(c)
t.end_fill()

#星
t.left(135)
x = h_m * 0.75
t.pencolor("#000000")
t.fillcolor("#000000")
t.penup()
t.goto(135,12)
t.pendown()
t.begin_fill()
for _ in range(5):
   t.forward(x)
   t.right(144)
t.end_fill()

t.penup()
t.goto(-100,12)
t.pendown()
t.begin_fill()
for _ in range(5):
   t.forward(x)
   t.right(144)
t.end_fill()


t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="圣多美和普林西比民主共和国国旗.eps") #将图片保存下来

turtle.done()