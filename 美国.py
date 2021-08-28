"""
 美国国旗
 美利坚合众国国旗形状是长方形；国旗的长宽之比为19:10，画面格局由两部分组成，旗的左上方方框上排列着50颗星，6颗一排与5颗一排相间排列，共排9行；旗的其余部分是13道横条 。
 美利坚合众国国旗颜色由红/白横条、白色星星、蓝色框构成
"""

import turtle
import math

w,h  = 950,500
item_h = h / 13
turtle.screensize(w,h,"white")
turtle.setup(w,h)

turtle.setup(width=w, height=h)  # 设置画布大小

t = turtle.Turtle()
t.pensize(1)
t.speed(0)


#条纹
colors = ["#bc133e","#ffffff"]

for j in range(0,13):
    t.pencolor(colors[j % 2])
    t.fillcolor(colors[j % 2])
    t.penup()
    t.goto(-w / 2, h / 2 - j * item_h)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        if i % 2 == 0:
            t.fd(w)
        else:
            t.fd(item_h)
        t.right(90)
    t.end_fill()

#蓝
t.penup()
t.goto(-w / 2, h / 2)
t.pendown()
t.color('#3c3b6e') 
t.begin_fill()
for i in range(4):
    if i % 2 == 0:
        t.fd(item_h * 10)
    else:
        t.fd(item_h * 7)
    t.right(90)
t.end_fill()

#星

# 五角星所在圆的半径 r=0.0308*k,求五角星前进边长qj
r = 0.0308 * h
qj = 2 * math.cos(math.radians(18)) * r  # 一笔贯通长度
qj2 = math.cos(math.radians(54)) * r / math.cos(math.radians(36))

#2画
#https://www.jianshu.com/p/024a9e082d42#comments
# 画星星
def star(x, y):
    t.setheading(0)
    t.penup()
    t.goto(x, y)
    t.right(198)
    t.fd(r)
    t.right(162)
    t.pendown()
    t.begin_fill()
    for i in range(5):
        t.fd(qj)
        t.right(144)
    t.end_fill()

t.pencolor("white")
t.fillcolor("white")
t.penup()
t.goto(-w / 2, h / 2)
t.pendown()
for i in range(1, 12, 2):
    for j in range(1, 10, 2):
        star(-(w / 2 - i * (2 / 5 * w) / 12), h / 2 - j * (7 / 13 * h) / 10)

t.penup()
t.goto(-(w / 2 - 2 * (2 / 5 * w) / 12), h / 2 - 2 * (7 / 13 * h) / 10)
t.pendown()
for i in range(2, 12, 2):
    for j in range(2, 10, 2):
        star(-(w / 2 - i * (2 / 5 * w) / 12), h / 2 - j * (7 / 13 *h) / 10)

t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="美国国旗.eps") #将图片保存下来

turtle.mainloop()
