"""
希腊国旗
希腊国旗（希腊语：Σημαία της Ελλάδος，通常被称为Γαλανόλευκη或Κυανόλευκη意“蓝白”），是由蓝白二色、十字图案及平行长条所构成的旗帜。
亦是希腊的旧军旗。9条蓝白相间的平行长条象征希腊独立战争时的口号“Ελευθερία ή Θάνατος”（不自由，毋宁死）的9个音节（另一说是9长条象征9位希腊神话中的文艺女神）。
蓝十字象征在1821年土耳其独立起义之际，巴特拉的盖尔马诺斯府主教挥扬的白地蓝十字旗。官方标准的国旗比例是3：2。
9个长条的宽度分别是国旗宽度的1/9，左上角正方形区域的边长是国旗宽度的5/9.
"""

import turtle

w = 900
h = 600
item = h / 9

turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)

#条纹
colors = ["#0d5eaf","#ffffff"]
for j in range(0,9):
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

#蓝
t.penup()
t.goto(-w/2,h/2)
t.pendown()
t.pensize(0)
t.pencolor("#0d5eaf")
t.fillcolor("#0d5eaf")
t.begin_fill()
for i in range(4):
    t.fd(item*5)
    t.right(90)
t.end_fill()

#十字
t.pencolor("white")
t.fillcolor("white")
t.penup()
t.home()
t.goto(-w/2 ,h / 2 - 2 * item )
t.pendown()

t.begin_fill()
for i in range (12):
    if i in (2,5,8,11):
        t.fd(item)
    else:
        t.fd(item * 2)
    if i % 3 == 0:
        t.left(90)
    else:        
        t.right(90)
t.end_fill()

# t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="希腊国旗.eps") #将图片保存下来

turtle.done()