"""
冰岛
冰岛国旗（英语：The flag of Iceland，冰岛语：íslenskifáninn）于1944年6月17日冰岛成为共和国时正式采用，设计为蓝色底色配以白色及红色的十字。
冰岛的第一面国旗最早出现于1897年的一次游行中，是一面深蓝色底绘有白色十字的旗帜。这面旗帜在1918年冰岛从丹麦独立时被定为冰岛的国旗。
对于冰岛人来说这面旗帜的色彩象征着冰岛的景色，三种色彩分别象征着组成冰岛的三种元素：红色象征冰岛火山中的火焰；白色象征覆盖冰岛的冰雪；蓝色则象征大西洋。
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
t.pencolor("#03539c")
t.fillcolor("#03539c")
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

#纵白
t.penup()
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
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


#横白
t.penup()
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
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
t.pencolor("#db1e34")
t.fillcolor("#db1e34")
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
t.pencolor("#db1e34")
t.fillcolor("#db1e34")
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
ts.getcanvas().postscript(file="冰岛国旗.eps") #将图片保存下来

turtle.done()