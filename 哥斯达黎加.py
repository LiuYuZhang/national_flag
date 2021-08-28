"""
哥斯达黎加国旗
哥斯达黎加共和国（The Republic of Costa Rica），简称哥斯达黎加，是位于拉丁美洲的一个总统共和制国家，北邻尼加拉瓜，南与巴拿马接壤，首都圣何塞。
哥斯达黎加国旗启用于1906年11月27日，国旗呈长方形，长与宽之比约为5:3。旗面自上而下由蓝、白、红、白、蓝五条平行宽条相连组成。红色宽条比蓝白色宽一倍。
蓝、白两色来自原中美洲联邦国旗的颜色，红色部分是1848年建立共和国时增加的。蓝色代表天空、机会、理想主义和坚忍；红色代表热忱和为独立所流的血；白色代表和平、智慧和快乐。
红色部分左侧处绘有国徽图案是政府用国旗，且政府用国旗比例为2:3。
"""

import turtle

width = 900
height = 540
turtle.screensize(width,height,"white")
turtle.setup(width=width,height=height)

item = height / 6

t = turtle.Turtle()
t.pensize(1)
t.speed(10)


#蓝
t.pencolor("#012b7f")
t.fillcolor("#012b7f")
t.forward(width/2)
t.left(90)
t.begin_fill()
t.forward(height/2)
t.left(90)
t.forward(width)
t.left(90)
t.forward(height)
t.left(90)
t.forward(width)
t.left(90)
t.forward(height/2)
t.end_fill()

# #白色
t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.forward(item * 2)
t.left(90)
t.forward(width)
t.left(90)
t.forward(item * 4)
t.left(90)
t.forward(width)
t.left(90)
t.forward(item *4)
t.end_fill()

# #红色
t.left(180)
t.forward(item)
t.pencolor("#ce1127")
t.fillcolor("#ce1127")
t.begin_fill()
t.right(90)
t.forward(width)
t.left(90)
t.forward(item*2)
t.left(90)
t.forward(width)
t.left(90)
t.forward(item*2)
t.end_fill()

t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="哥斯达黎加国旗.eps") #将图片保存下来

turtle.done()
