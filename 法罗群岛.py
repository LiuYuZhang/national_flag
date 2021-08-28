"""
挪威国旗
挪威国旗呈长方形，长宽之比为11：8。红色旗面，偏左侧绘有蓝白色十字。挪威曾为丹麦所统治，国旗十字的来历与丹麦国旗的十字来历相同。
蓝、白、红象征着自由与独立。它的国旗有两种，政府机构悬挂燕尾式国旗，其他场合悬挂上述横长方形国旗。
国旗不同颜色的宽度比例是6-1-2-1-12，高度比例是6-1-2-1-6 
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
t.pencolor("#ef2b2d")
t.fillcolor("#ef2b2d")
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
t.pencolor("white")
t.fillcolor("white")
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


#纵蓝
t.penup()
t.pencolor("#002768")
t.fillcolor("#002768")
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

#横蓝
t.penup()
t.pencolor("#002768")
t.fillcolor("#002768")
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

ts = t.getscreen()
ts.getcanvas().postscript(file="挪威国旗.eps") #将图片保存下来

turtle.done()