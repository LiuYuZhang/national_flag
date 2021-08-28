"""
法罗群岛
与挪威和冰岛国旗一样，法罗群岛的地区旗帜也使用了白色、蓝色和红色。白色，象征晴朗的天空以及拍打着群岛的浪花；蓝色和红色，则源自当地人传统头饰。
"""

import turtle

w = 880
h = 640
item_w = w / 26
item_h = h / 16


turtle.screensize(w,h,"white")
turtle.setup(w,h)
t = turtle.Turtle()
t.speed(10)
t.pensize(1)


#底色框
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
t.penup()
t.goto(-w/2,-h / 2)
t.pendown()
t.begin_fill()
t.forward(w)
t.left(90)
t.forward(h)
t.left(90)
t.forward(w)
t.end_fill()

#纵蓝
t.penup()
t.pencolor("#0065bd")
t.fillcolor("#0065bd")
t.goto(- item_w * 6, h/2)
t.pendown()
t.begin_fill()
for i in range(4):
    t.left(90)
    if i % 2 == 0:
        t.fd(h)
    else:
        t.fd(item_w * 4)
t.end_fill()


#横蓝
t.penup()
t.pencolor("#0065bd")
t.fillcolor("#0065bd")
t.home()
t.goto(- w / 2, item_h * 2)
t.pendown()
t.begin_fill()
for i in range(4):
    if i % 2 == 0:
        t.fd(w)
    else:
        t.fd(item_h * 4)
    t.right(90)
t.end_fill()


#纵红
t.penup()
t.pencolor("#ed2939")
t.fillcolor("#ed2939")
t.home()
t.goto(- item_w * 5, h/2)
t.pendown()
t.begin_fill()
for i in range(4):
    if i % 2 == 0:
        t.fd(item_w * 2)
    else:
        t.fd(h)
    t.right(90)
t.end_fill()

#横红
t.penup()
t.pencolor("#ed2939")
t.fillcolor("#ed2939")
t.home()
t.goto(- w / 2, item_h)
t.pendown()
t.begin_fill()
for i in range(4):
    if i % 2 == 0:
        t.fd(w)
    else:
        t.fd(item_h * 2)
    t.right(90)
t.end_fill()

t.hideturtle()
ts = t.getscreen()
ts.getcanvas().postscript(file="法罗群岛.eps") #将图片保存下来

turtle.done()