"""
巴哈马国旗
巴哈马国旗启用于1973年7月10日，国旗呈长方形，长宽之比为2：1。旗面由黑黄蓝三色组成。黄色象征这个岛国的沙滩；黑色三角形象征巴哈马人民团结一致，开发利用岛国的海陆资源
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

#蓝
t.pencolor("#00abc9")
t.fillcolor("#00abc9")
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
t.pencolor("#fae043")
t.fillcolor("#fae043")
t.penup()
t.goto(0,-h_m/2)
t.pendown()
t.forward(w/2)
t.begin_fill()
t.left(90)
t.forward(h_m)
t.left(90)
t.forward(w)
t.left(90)
t.forward(h_m)
t.left(90)
t.forward(h / 2)
t.end_fill()

#蓝
t.pencolor("#00abc9")
t.fillcolor("#00abc9")
t.penup()
t.goto(0,-h_m-h_m/2)
t.pendown()

t.begin_fill()
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

#红色三角形
t.penup()
t.goto(-w/2,h/2)
t.pendown()
t.pencolor("#000000")
t.fillcolor("#000000")
t.begin_fill()
t.right(30)
t.fd(h)
t.right(120)
t.fd(h)
t.end_fill()


t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="巴哈马国旗.eps") #将图片保存下来

turtle.done()