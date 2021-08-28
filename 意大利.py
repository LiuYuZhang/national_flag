"""
意大利国旗
意大利共和国（意大利语：Repubblica Italiana），简称意大利（意大利语：Italia），是一个欧洲国家，主要由南欧的亚平宁半岛及两个位于地中海中的岛屿西西里岛与萨丁岛所组成。
意大利首都罗马，几个世纪一直都是西方文明的中心。意大利国旗呈长方形，长与宽之比为3∶2。旗面由三个平行相等的竖长方形相连构成，从左至右依次为绿、白、红三色。
意大利原来国旗的颜色与法国国旗相同，1796年才把蓝色改为绿色。
据记载，1796年拿破仑的意大利军团在征战中曾使用由拿破仑本人设计的绿、白、红三色旗。1946年意大利共和国建立，正式规定绿、白、红三色旗为共和国国旗。
"""

import turtle
from typing import ItemsView

w = 900
h = 600
item = w / 3

turtle.screensize(w,h,"white")
turtle.setup(w,h)

#绿
t = turtle.Turtle()
t.pensize(1)
t.speed(10)

t.pencolor("#009246")
t.fillcolor("#009246")
t.penup()
t.goto(-item/2,0)
t.pendown()
t.begin_fill()
t.left(90)
t.forward(h//2)
t.left(90)
t.fd(item)
t.left(90)
t.fd(h)
t.left(90)
t.fd(item)
t.end_fill()

#白
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
t.begin_fill()
t.forward(item)
t.left(90)
t.fd(h)
t.left(90)
t.fd(item)
t.left(90)
t.end_fill()
t.right(270)
t.forward(item)

#红
t.pencolor("#ce2b37")
t.fillcolor("#ce2b37")
t.begin_fill()
t.fd(item)
t.right(90)
t.fd(h)
t.right(90)
t.fd(item)
t.end_fill()

t.hideturtle()

turtle.done()

