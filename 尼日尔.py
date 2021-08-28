"""
尼日尔国旗
尼日尔共和国（The Republic of Niger），简称尼日尔，位于非洲中西部，是撒哈拉沙漠南缘的内陆国，官方语言为法语，首都尼亚美。
尼日尔国旗呈长方形，长与宽之比约为7：6。自上而下由橙、白、绿三个平行相等的横长方形组成，白色部分中间有一橙色圆轮。
橙色象征撒哈拉沙漠；白色象征纯洁；绿色代表美丽富饶的土地，也象征博爱和希望。圆轮象征太阳，还象征尼日尔人民为保护自己的权力而不惜牺牲的愿望。
"""

import turtle
from typing import ItemsView

width = 700
height = 600
turtle.screensize(width,height,"white")
turtle.setup(width=width,height=height)
item = height / 3

t = turtle.Turtle()
t.pensize(1)
t.speed(10)


#橙色
t.penup()
t.goto(0,height/2)
t.pendown()
t.pencolor("#e05206")
t.fillcolor("#e05206")
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

#白色
t.penup()
t.goto(0,height/2 - item)
t.pendown()
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
t.begin_fill()
t.forward(width/2)
t.right(90)
t.forward(item)
t.right(90)
t.forward(width)
t.right(90)
t.forward(item)
t.right(90)
t.end_fill()


#绿色
t.penup()
t.goto(0,-height/2)
t.pendown()

t.pencolor("#0db02b")
t.fillcolor("#0db02b")
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


#明月
t.pencolor("#e05206")
t.fillcolor("#e05206")
t.penup()
t.goto(0,-item / 2*0.86)
t.pendown()

t.begin_fill()
t.circle(item / 2 *0.86)
t.end_fill()

t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="尼日尔国旗.eps") #将图片保存下来

turtle.done()
