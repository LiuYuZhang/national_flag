"""
几内亚比绍国旗
几内亚比绍国旗启用于1973年。国旗呈长方形，长与宽之比为2：1。由红、黄、绿、黑四色组成。靠旗杆一侧为红色竖长方形，中央有一颗黑色五角星；旗面右侧为两个平行相等的横长方形，上黄下绿。
"""

import turtle

w = 900
h = 450
turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)

#黄
t.pencolor("#fdd116")
t.fillcolor("#fdd116")
t.begin_fill()
t.forward(w/2)
t.left(90)
t.forward(h/2)
t.left(90)
t.forward(w)
t.left(90)
t.forward(h/2)
t.left(90)
t.forward(w/2)
t.end_fill()


#绿
t.pencolor("#009e49")
t.fillcolor("#009e49")
t.begin_fill()
t.penup()
t.goto(0,-h/2)
t.pendown()
t.forward(w/2)
t.left(90)
t.forward(h/2)
t.left(90)
t.forward(w)
t.left(90)
t.forward(h/2)
t.left(90)
t.forward(w/2)
t.end_fill()

#红
t.penup()
t.goto(-w / 2,0)
t.pendown()
t.pencolor("#ce1127")
t.fillcolor("#ce1127")
t.begin_fill()
t.left(90)
t.fd(h/2)
t.right(90)
t.fd(w/3)
t.right(90)
t.fd(h)
t.right(90)
t.fd(w/3)
t.end_fill()


#星
t.left(180)
t.pencolor("#000000")
t.fillcolor("#000000")
t.penup()
t.goto(-w /2 + w / 2 /3 - 50,25)
t.pendown()
t.begin_fill()
for _ in range(5):
   t.forward(100)
   t.right(144)
t.end_fill()

t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="几内亚比绍国旗.eps") #将图片保存下来

turtle.done()