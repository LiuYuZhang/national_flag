"""
朝鲜国旗
根据《朝鲜民主主义人民共和国社会主义宪法》第148条规定，朝鲜民主主义人民共和国国旗，中间是红色宽面，其上下各有一白色细条，再上下是蓝色宽边，红色靠旗杆一边有一白色圆地，其中为红色五角星。
旗幅长宽比例为2:1。
https://baike.baidu.com/item/%E6%9C%9D%E9%B2%9C%E6%B0%91%E4%B8%BB%E4%B8%BB%E4%B9%89%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E5%9B%BD%E6%97%97/1103603?from=kg_qa
"""

import turtle
import math

w = 864
h = 432
item = w / 144 

turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)

#蓝
t.pencolor("#024fa1")
t.fillcolor("#024fa1")
t.penup()
t.goto(w/2,h/2)
t.pendown()
t.begin_fill()
for i in range(4):
    t.right(90)
    if i % 2 == 0:
        t.fd(item * 12)
    else:
        t.fd(w)
t.end_fill()



#白
t.pencolor("white")
t.fillcolor("white")
t.penup()
t.home()
t.goto(w/2,h/2 - item * 12)
t.pendown()
t.begin_fill()
for i in range(4):
    t.right(90)
    if i % 2 == 0:
        t.fd(item * 2)
    else:
        t.fd(w)
t.end_fill()


#红
t.pencolor("#ee1c27")
t.fillcolor("#ee1c27")
t.penup()
t.home()
t.goto(w/2, h / 2 - item * 14)
t.pendown()
t.begin_fill()
for i in range(4):
    t.right(90)
    if i % 2 == 0:
        t.fd(item * 44)
    else:
        t.fd(w)
t.end_fill()

#白
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
t.penup()
t.home()
t.goto(w/2, - h / 2 + item * 14)
t.pendown()
t.begin_fill()
for i in range(4):
    t.right(90)
    if i % 2 == 0:
        t.fd(item * 2)
    else:
        t.fd(w)
t.end_fill()


#红
t.pencolor("#024fa1")
t.fillcolor("#024fa1")
t.penup()
t.home()
t.goto(w/2, - h / 2 + item * 12)
t.pendown()
t.begin_fill()
for i in range(4):
    t.right(90)
    if i % 2 == 0:
        t.fd(item * 12)
    else:
        t.fd(w)
t.end_fill()

#288
#432
#圆
t.penup()
t.right(90)
t.home()
t.setx(-(w / 2 - w / 144 * 48))
t.sety(- (16*item))
t.pendown()
t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.circle(16*item)
t.end_fill()


# #星
t.pencolor("#ee1c27")
t.fillcolor("#ee1c27")
t.penup()
t.home()
t.setx(-(w / 2 - w / 144 * 33))
t.sety(item * 5)
t.pendown()
t.begin_fill()
for _ in range(5):
   t.forward(item*30)
   t.right(144)
t.end_fill()

t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="朝鲜国旗.eps") #将图片保存下来

turtle.done()