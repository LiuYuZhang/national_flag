"""
罗马尼亚国旗
罗马尼亚（Romania），位于东南欧巴尔干半岛东北部。罗马尼亚国旗呈长方形，长宽之比为3：2。
由三个平行相等的竖长方形组成，从左至右依次为蓝、黄、红三色。蓝色象征蓝天，黄色象征丰富的自然资源，红色象征人民的勇敢和牺牲精神。
在民族色彩上，蓝色象征特兰西瓦尼亚、黄色象征瓦拉几亚，红色象征摩尔多瓦。1994年7月16日启用。除了和乍得国旗的蓝色色条有细微区别，其他一样。
"""

import turtle
from typing import ItemsView

w = 900
h = 600
item = w / 3

turtle.screensize(w,h,"white")
turtle.setup(w,h)

#蓝
t = turtle.Turtle()
t.pensize(1)
t.speed(10)

t.pencolor("#004890")
t.fillcolor("#004890")
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
t.pencolor("#fddf03")
t.fillcolor("#fddf03")
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
t.pencolor("#e51837")
t.fillcolor("#e51837")
t.begin_fill()
t.fd(item)
t.right(90)
t.fd(h)
t.right(90)
t.fd(item)
t.end_fill()

t.hideturtle()

turtle.done()

ts = t.getscreen()
ts.getcanvas().postscript(file="罗马尼亚国旗.eps") #将图片保存下来

