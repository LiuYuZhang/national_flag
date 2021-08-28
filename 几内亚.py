"""
几内亚国旗
几内亚共和国（The Republic of Guinea），简称几内亚，位于西非西岸，首都科纳克里。几内亚国旗启用于1958年11月10日。国旗呈长方形，长宽之比为3:2。
由三个平行相等的竖长方形组成，从左至右依次为红、黄、绿三色。红色象征为自由而斗争烈士的鲜血，还象征劳动者为建设祖国而作出的牺牲；黄色代表国家的黄金，也象征普照全国的阳光；绿色象征该国植物。
另外，红、黄、绿三色也是泛非颜色，几内亚人视之为“勤劳、正义、团结一致”的标志。
"""

import turtle
from typing import ItemsView

w = 900
h = 600
item = w / 3

turtle.screensize(w,h,"white")
turtle.setup(w,h)

#红
t = turtle.Turtle()
t.pensize(1)
t.speed(10)

t.pencolor("#ce1126")
t.fillcolor("#ce1126")
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
t.pencolor("#fcd116")
t.fillcolor("#fcd116")
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

#绿
t.pencolor("#009460")
t.fillcolor("#009460")
t.begin_fill()
t.fd(item)
t.right(90)
t.fd(h)
t.right(90)
t.fd(item)
t.end_fill()

t.hideturtle()

turtle.done()

