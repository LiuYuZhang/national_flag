"""
瑞士国旗
十字占整面国旗的5/8,长宽1:1
#https://baike.baidu.com/item/%E7%91%9E%E5%A3%AB%E8%81%94%E9%82%A6%E5%9B%BD%E6%97%97?fromtitle=%E7%91%9E%E5%A3%AB%E5%9B%BD%E6%97%97&fromid=1902299
"""

import turtle

h = 450
w = 450
item = h / 5

turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)

#红
t.pencolor("#FF0000")
t.fillcolor("#FF0000")
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


#十字
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
t.penup()
t.goto(-w/2 + item, item * 0.5)
t.pendown()

t.begin_fill()
for i in range (12):
    t.fd(item)
    if i % 3 == 0:
        t.left(90)
    else:
        t.right(90)
t.end_fill()
    

t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="瑞士国旗.eps") #将图片保存下来

turtle.done()