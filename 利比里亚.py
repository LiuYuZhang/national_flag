"""
利比里亚国旗
国旗呈横长方形，长与宽之比为19：10。由红、白相间的11道平行横条组成，左上角为蓝色正方形，内有一白色五角星。11道红白条纹是纪念利比里亚独立宣言的11个签字者。
"""

import turtle

h = 450
w = h / 10 * 19
item = h / 11

turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)

#条纹
colors = ["#be0a2f","#ffffff"]
for j in range(0,11):
    t.pencolor(colors[j % 2])
    t.fillcolor(colors[j % 2])
    t.penup()
    t.goto(w/2,h/2 - item * j)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.right(90)
        if i % 2 == 0:
            t.fd(item)
        else:
            t.fd(w)
    t.end_fill()

#红
t.penup()
t.goto(-w/2,h/2)
t.pendown()
t.pensize(0)
t.pencolor("#002768")
t.fillcolor("#002768")
t.begin_fill()
for i in range(4):
    t.fd(item*5)
    t.right(90)
t.end_fill()

#星
t.pencolor("white")
t.fillcolor("white")
t.penup()
t.home()
t.goto(-w/2 +  item,h / 2 - 2 * item )
t.pendown()
t.begin_fill()
for _ in range(5):
   t.forward(item * 3)
   t.right(144)
t.end_fill()

t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="利比里亚国旗.eps") #将图片保存下来

turtle.done()