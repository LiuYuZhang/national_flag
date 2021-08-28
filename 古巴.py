"""
古巴国旗
长方形，长与宽之比为2：1。旗面左侧为红色等边三角形，内有一颗白色五角星；旗面右侧由三道蓝色宽条和两道白色宽条平行相间、相连构成。五角星代表古巴是一个独立的民族。
三角形和星是古巴秘密革命组织的标志，象征自由、平等、博爱和爱国者的鲜血。
五角星还代表古巴是一个独立的民族。三道蓝色宽条表示古巴形成时由三部分组成，白条表示古巴人民的纯洁理想。
"""

import turtle
import math

w = 900
h = 450
h_m = h/5

turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)

#绿
t.pencolor("#002a90")
t.fillcolor("#002a90")

t.penup()
t.goto(w/ 2,h/2)
t.pendown()
t.begin_fill()
for i in range(1,4):
       t.right(90)
       if i % 2 == 0:
              t.fd(w)
       else:
              t.fd(h_m)
t.end_fill()



#白
t.pencolor("white")
t.fillcolor("white")
t.penup()
t.goto(w/ 2,2 * h_m - h_m / 2)
t.pendown()
t.begin_fill()
for i in range(1,4):
       t.left(90)
       if i % 2 == 0:
              t.fd(h_m)
       else:
              t.fd(w)
t.end_fill()

#绿
t.pencolor("#002a90")
t.fillcolor("#002a90")
t.penup()
t.goto(w/ 2, -h_m /2)
t.pendown()
t.begin_fill()
for i in range(1,4):
       t.left(90)
       if i % 2 == 0:
              t.fd(w)
       else:
              t.fd(h_m)
t.end_fill()


#白
t.pencolor("white")
t.fillcolor("white")
t.penup()
t.goto(w/ 2,- h_m - h_m / 2)
t.pendown()
t.begin_fill()
for i in range(1,4):
       t.right(90)
       if i % 2 == 0:
              t.fd(h_m)
       else:
              t.fd(w)
t.end_fill()


#绿
t.pencolor("#002a90")
t.fillcolor("#002a90")
t.penup()
t.goto(w/ 2, - 2 * h_m  -h_m /2)
t.pendown()
t.begin_fill()
for i in range(1,4):
       t.left(90)
       if i % 2 == 0:
              t.fd(w)
       else:
              t.fd(h_m)
t.end_fill()



#红色等边三角形
t.penup()
t.goto(-w/2,h/2)
t.right(270)
t.pendown()
t.pencolor("#d21034")
t.fillcolor("#d21034")
t.begin_fill()
t.right(30)
t.fd(h)
t.right(120)
t.fd(h)
t.end_fill()

#星
x = h_m * 1.5
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
t.penup()
t.home()
t.goto(-370,15)
t.pendown()
t.begin_fill()
for _ in range(5):
   t.forward(x)
   t.right(144)
t.end_fill()


t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="古巴国旗.eps") #将图片保存下来

turtle.done()