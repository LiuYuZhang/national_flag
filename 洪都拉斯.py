"""
洪都拉斯国旗
洪都拉斯国旗启用于1949年1月18日，国旗呈长方形，长宽之比为2：1。旗面自上而下由蓝、白、蓝三个平行相等的长方形组成。白色长方形中间有五颗蓝色五角星。
"""

import turtle

w = 900
h = 450
turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)

#蓝
t.pencolor("#0073cf")
t.fillcolor("#0073cf")
t.begin_fill()
t.penup()
t.goto(0,h/3/2)
t.pendown()
t.forward(w/2)
t.left(90)
t.forward(h/3)
t.left(90)
t.forward(w)
t.left(90)
t.forward(h/3)
t.left(90)
t.forward(w/2)
t.end_fill()


#白
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
t.begin_fill()
t.penup()
t.goto(0,-h/3/2)
t.pendown()
t.forward(w/2)
t.left(90)
t.forward(h/3)
t.left(90)
t.forward(w)
t.left(90)
t.forward(h/3)
t.left(90)
t.forward(w/2)
t.end_fill()

#蓝
t.pencolor("#0073cf")
t.fillcolor("#0073cf")
t.begin_fill()
t.penup()
t.goto(0,-h/3-h/3/2)
t.pendown()
t.forward(w/2)
t.left(90)
t.forward(h/3)
t.left(90)
t.forward(w)
t.left(90)
t.forward(h/3)
t.left(90)
t.forward(w/2)
t.end_fill()

#星
x = 40
t.pencolor("#0073cf")
t.fillcolor("#0073cf")
t.penup()
t.goto(-20,10)
t.pendown()
t.begin_fill()
for _ in range(5):
   t.forward(x)
   t.right(144)
t.end_fill()

#星-右
t.penup()
t.goto(90,45)
t.pendown()
t.begin_fill()
for _ in range(5):
   t.forward(x)
   t.right(144)
t.end_fill()

t.penup()
t.goto(90,-25)
t.pendown()
t.begin_fill()
for _ in range(5):
   t.forward(x)
   t.right(144)
t.end_fill()


#星-左
t.penup()
t.goto(-90-x,45)
t.pendown()
t.begin_fill()
for _ in range(5):
   t.forward(x)
   t.right(144)
t.end_fill()

t.penup()
t.goto(-90-x,-25)
t.pendown()
t.begin_fill()
for _ in range(5):
   t.forward(x)
   t.right(144)
t.end_fill()

t.hideturtle()
ts = t.getscreen()
ts.getcanvas().postscript(file="洪都拉斯国旗.eps") #将图片保存下来

turtle.done()