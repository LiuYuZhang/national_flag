"""
汤加国旗
长方形，长宽之比为2：1。红色旗面，左上角白色长方形上有一个红色十字。红色象征基督所洒下的鲜血，十字表示信奉基督教。
"""

import turtle

h = 450
w = 900

turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)

#红
t.pencolor("#c10100")
t.fillcolor("#c10100")
t.penup()
t.goto(w/2,h/2)
t.pendown()
t.begin_fill()
for i in range(4):
    t.right(90)
    if i % 2 == 0:
        t.fd(h)
    else:
        t.fd(w)
t.end_fill()

#白
t.penup()
t.goto(-w/2,h/2)
t.pendown()
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
t.begin_fill()
for i in range(4):
    if i % 2 == 0:
        t.fd(w*0.4)
    else:
        t.fd(h * 0.5)
    t.right(90)
t.end_fill()

#十字
t.pencolor("#c10100")
t.fillcolor("#c10100")
t.penup()
t.goto(-w/2 * 0.76,((3*50)-20))
t.pendown()

t.begin_fill()
for i in range (12):
    t.fd(50)
    if i % 3 == 0:
        t.left(90)
    else:
        t.right(90)
t.end_fill()
    

t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="汤加国旗.eps") #将图片保存下来

turtle.done()