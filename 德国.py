"""
 德国国旗
 德意志联邦共和国（Federal Republic of Germany），简称德国（Germany）。是位于中欧的联邦议会共和制国家，是欧洲联盟中人口最多的国家，以德意志人为主体民族，首都柏林。
 德国国旗呈长方形，长与宽之比为5∶3。自上而下由黑、红、金三个平行相等的横长方形相连而成。
 三色旗的来历众说纷纭，最早可追溯到公元一世纪的古罗马帝国，在后来16世纪的德国农民战争和17世纪的德国资产阶级民主革命中，代表共和制的三色旗也飘扬在德意志大地上。
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

#顶部黑色
t.pencolor("#000000")
t.fillcolor("#000000")
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


#中间红色
t.pencolor("#dd0000")
t.fillcolor("#dd0000")
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

#底部金色
t.pencolor("#ffce00")
t.fillcolor("#ffce00")
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
ts.getcanvas().postscript(file="德国国旗.eps") #将图片保存下来

turtle.done()