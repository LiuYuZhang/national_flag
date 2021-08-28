"""
喀麦隆国旗
喀麦隆共和国通称喀麦隆，是位于非洲中西部的单一制共和国，首都是雅温得。喀麦隆国旗采用于1975年5月20日，是一面三色旗。
由绿、红、黄三直条组成，中有一黄星，星的尺寸没有明确规定，故有所不同，但一定在中央。
国旗呈长方形，长与宽之比为3∶2。从左至右由绿、红、黄三个平行相等的竖长方形组成，红色部分中间有一颗黄色五角星。
绿色象征南部赤道雨林的热带植物，还象征人民对幸福未来的希望；黄色象征北部草原和矿产资源，也象征给人民带来幸福的太阳光辉；红色象征联合统一的力量。
五角星象征国家的统一。
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

t.pencolor("#007a5e")
t.fillcolor("#007a5e")
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

#红
t.pencolor("#ce1126")
t.fillcolor("#ce1126")
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

#黄
t.pencolor("#fcd116")
t.fillcolor("#fcd116")
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
t.pencolor("#fcd116")
t.fillcolor("#fcd116")
t.begin_fill() #填充颜色开始
for _ in range(5):
   t.forward(160)
   t.right(144)
t.end_fill() #填充图形颜色前调用

t.hideturtle()


ts = t.getscreen()
ts.getcanvas().postscript(file="喀麦隆国旗.eps") #将图片保存下来

turtle.done()

