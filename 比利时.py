"""
比利时国旗
比利时王国（法语：Belgique，德语：Belgien），简称“比利时”，位于欧洲西部沿海。比利时国旗呈长方形，长与宽之比为15:13。旗面从左到右由黑、黄、红三个平行相等的竖长方形相连构成。
黑色是庄重而具有纪念意义的色彩，表示悼念在1830年独立战争中牺牲的英雄；黄色象征国家的财富和畜牧业与农业的丰收；红色象征爱国者的生命和热血，还象征独立战争取得的伟大胜利。
比利时是世袭君主立宪制国家。国王乘坐的汽车悬挂王旗，王旗与国旗不同，为四方形，旗地近似咖啡色，旗中间有比利时国徽，旗地四角处各有一顶王冠和在位国王名字的第一个字母。
"""

import turtle
from typing import ItemsView

w = 900
h = 780
item = w / 3

turtle.screensize(w,h,"white")
turtle.setup(w,h)

#黑
t = turtle.Turtle()
t.pensize(1)
t.speed(10)

t.pencolor("black")
t.fillcolor("black")
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
t.pencolor("#fae042")
t.fillcolor("#fae042")
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
t.pencolor("#ed2939")
t.fillcolor("#ed2939")
t.begin_fill()
t.fd(item)
t.right(90)
t.fd(h)
t.right(90)
t.fd(item)
t.end_fill()

t.hideturtle()



turtle.done()

