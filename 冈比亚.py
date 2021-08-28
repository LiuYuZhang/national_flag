"""
冈比亚国旗
冈比亚共和国（Republic of The Gambia），简称冈比亚，首都是班珠尔。冈比亚国旗启用于1965年2月18日。呈长方形，长与宽之比为3:2。
自上而下由红、蓝、绿三个平行横长方形组成，蓝色与红、绿色交接处各有一道白条。
红色象征阳光；蓝色象征爱与忠诚，还代表横贯全国东西的冈比亚河；绿色象征宽容，也象征农业；两道白条表示纯洁、和平、遵守法律，以及冈比亚人对世界人民的友好感情。
"""

import turtle
from typing import ItemsView

width = 900
height = 600
turtle.screensize(width,height,"white")
turtle.setup(width=width,height=height)

white_h = height * 0.26
red = green =  height * 0.37

t = turtle.Turtle()
t.pensize(1)
t.speed(10)


#画红色
t.penup()
t.goto(0,height/2)
t.pendown()
t.pencolor("#ce1126")
t.fillcolor("#ce1126")
t.left(90)
t.begin_fill()
t.right(90)
t.forward(width/2)
t.right(90)
t.forward(red)
t.right(90)
t.forward(width)
t.right(90)
t.forward(red)
t.right(90)
t.forward(width/2)
t.end_fill()

#白色
t.penup()
t.goto(0,height/2 - red)
t.pendown()
t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.forward(width/2)
t.right(90)
t.forward(white_h)
t.right(90)
t.forward(width)
t.right(90)
t.forward(white_h)
t.right(90)
t.end_fill()

# #蓝色
t.pencolor("#0c1c8c")
t.fillcolor("#0c1c8c")
t.penup()
t.goto(0,white_h * 0.68/2)
t.pendown()
t.begin_fill()
t.forward(width /2)
t.right(90)
t.forward(white_h*0.68)
t.right(90)
t.forward(width)
t.right(90)
t.forward(white_h*0.68)
t.right(90)
t.forward(width /2)
t.end_fill()

#绿色
t.penup()
t.goto(0,-height/2)
t.pendown()

t.pencolor("#3a7728")
t.fillcolor("#3a7728")
t.begin_fill()
t.fd(width / 2)
t.left(90)
t.fd(green)
t.left(90)
t.fd(width)
t.left(90)
t.fd(green)
t.left(90)
t.fd(width / 2)
t.end_fill()

t.hideturtle()


ts = t.getscreen()
ts.getcanvas().postscript(file="冈比亚国旗.eps") #将图片保存下来

turtle.done()
