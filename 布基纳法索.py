"""
布基纳法索国旗
布基纳法索（Burkina Faso），是位于非洲西部沃尔特河上游的内陆国，首都瓦加杜古。布基纳法索国旗启用于1984年8月4日。
国旗呈长方形，长宽之比为3:2。由上红下绿两个平行相等的横长方形组成，旗面中央有一颗金黄色的五角星。
红色象征革命，绿色象征农业、土地和希望；五角星象征革命向导，金黄色象征财富。
"""

import turtle
from typing import ItemsView

width = 700
height = 600
turtle.screensize(width,height,"white")
turtle.setup(width=width,height=height)
item = height / 2

t = turtle.Turtle()
t.pensize(1)
t.speed(10)


#红色
t.penup()
t.goto(0,height/2)
t.pendown()
t.pencolor("#ef2b2d")
t.fillcolor("#ef2b2d")
t.left(90)
t.begin_fill()
t.right(90)
t.forward(width/2)
t.right(90)
t.forward(item)
t.right(90)
t.forward(width)
t.right(90)
t.forward(item)
t.right(90)
t.forward(width/2)
t.end_fill()



#绿色
t.penup()
t.goto(0,-height/2)
t.pendown()

t.pencolor("#009e49")
t.fillcolor("#009e49")
t.begin_fill()
t.fd(width / 2)
t.left(90)
t.fd(item)
t.left(90)
t.fd(width)
t.left(90)
t.fd(item)
t.left(90)
t.fd(width / 2)
t.end_fill()


#星
t.penup()
t.goto(-80,34)
t.pendown()
t.pencolor("#fcd116")
t.fillcolor("#fcd116")
t.begin_fill() #填充颜色开始
for _ in range(5):
   t.forward(160)
   t.right(144)
t.end_fill() #填充图形颜色前调用



t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="布基纳法索国旗.eps") #将图片保存下来

turtle.done()
