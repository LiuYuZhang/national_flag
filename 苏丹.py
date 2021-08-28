"""
苏丹国旗
苏丹国旗呈横长方形，长与宽之比为2∶1。靠旗杆一侧为绿色等腰三角形，右侧为三个平行且宽度相等的宽条，自上而下依次为红、白、黑三色。
红色象征革命，白色象征和平，黑色象征属非洲黑色人种的南方居民，绿色象征北方居民所信奉的伊斯兰教。
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

#红
t.pencolor("#d21033")
t.fillcolor("#d21033")
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

#黑
t.pencolor("#000000")
t.fillcolor("#000000")
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
t.pencolor("#00722a")
t.fillcolor("#00722a")
t.begin_fill()
t.right(45)
t.fd(c)
t.right(90)
t.fd(c)
t.end_fill()

t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="苏丹国旗.eps") #将图片保存下来

turtle.done()