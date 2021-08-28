"""
也门国旗
也门共和国（Yemen Republic），位于阿拉伯半岛西南端，与沙特、阿曼相邻，濒红海、亚丁湾和阿拉伯海。也门国旗是一面红白黑三色横条组成的旗帜。
1990年5月22日启用。国旗呈长方形，长宽之比为3：2。旗面自上而下有红、白、黑三个相等的长方形组成。红色象征革命和胜利。白色象征神圣与纯洁。黑色象征过去的黑暗时代。
"""

import turtle

w = 900
h = 600
turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)
t.hideturtle()

#顶部红色
t.pencolor("#ce1127")
t.fillcolor("#ce1127")
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


#中间白色
t.pencolor("white")
t.fillcolor("white")
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

#底部黑色
t.pencolor("#000000")
t.fillcolor("#000000")
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
ts = t.getscreen()
ts.getcanvas().postscript(file="也门国旗.eps") #将图片保存下来

turtle.done()