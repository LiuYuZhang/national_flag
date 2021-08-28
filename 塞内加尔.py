"""
塞内加尔国旗
塞内加尔共和国（The Republic of Senegal），简称塞内加尔，位于非洲西部凸出部位的最西端，首都达喀尔。塞内加尔国旗启用于1960年8月20日，国旗呈长方形，长与宽之比为3:2。
旗面由三个平行相等的竖长方形构成，从左至右依次为绿、黄、红三色，黄色长方形中间有一个绿色五角星。
绿色象征国家的农业、植物和森林，黄色象征丰富的自然资源，红色象征为争取独立自由而斗争的烈士的鲜血；绿、黄、红色也是传统的泛非颜色。绿色五角星象征非洲的自由。
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

t.pencolor("#00853f")
t.fillcolor("#00853f")
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

#黄
t.pencolor("#fdef42")
t.fillcolor("#fdef42")
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
t.pencolor("#e31b23")
t.fillcolor("#e31b23")
t.begin_fill()
t.fd(item)
t.right(90)
t.fd(h)
t.right(90)
t.fd(item)
t.end_fill()


#星
t.right(180)
t.penup()
t.goto(-80,40)
t.pendown()
t.pencolor("#00853f")
t.fillcolor("#00853f")
t.begin_fill() #填充颜色开始
for _ in range(5):
   t.forward(160)
   t.right(144)
t.end_fill() #填充图形颜色前调用

t.hideturtle()


ts = t.getscreen()
ts.getcanvas().postscript(file="塞内加尔国旗.eps") #将图片保存下来

turtle.done()

