"""
智利国旗
智利共和国（Republic of Chile），简称智利，位于南美洲西南部，安第斯山脉西麓，首都圣地亚哥。智利国旗启用于1817年10月18日，国旗呈长方形，长宽之比为3:2。
旗面由蓝、白、红三色组成。上半部左角为蓝色正方形，其中央绘有一颗白色五角星。右侧为白色长方形。下半部为红色长方形。白色部分等于红色部分的2/3。
红色象征为了智利的独立和自由，为了反抗西班牙殖民军的统治，在兰卡瓜英勇牺牲的烈士鲜血。白色象征安第斯山高峰的白雪。
蓝色象征海洋。智利国旗是在独立之初，以美国星条旗为本而设计的。红色代表为脱离西班牙而流的鲜血。蓝色代表智利的天空与海洋颜色，正方形据说是取自印第安徽章。
白色是安地斯山的雪。星星指南天光辉的星星，表示国家统一。
"""

import turtle
from typing import ItemsView

w = 900
h = 600
turtle.screensize(w,h,"white")
turtle.setup(w,h)
blue = w / 3

t = turtle.Turtle()
t.pensize(1)
t.speed(10)

#顶部白色
t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.forward(w/2)
t.left(90)
t.forward(h/2)
t.left(90)
t.forward(w)
t.left(90)
t.forward(h/2)
t.left(90)
t.forward(w/2)
t.end_fill()


#底部红色
t.pencolor("#d52b1e")
t.fillcolor("#d52b1e")
t.begin_fill()
t.penup()
t.goto(0,-h/2)
t.pendown()
t.forward(w/2)
t.left(90)
t.forward(h/2)
t.left(90)
t.forward(w)
t.left(90)
t.forward(h/2)
t.left(90)
t.forward(w/2)
t.end_fill()


#蓝
t.penup()
t.goto(-w /2 + blue, h / 2 - blue)
t.pendown()
t.pencolor("#0039a6")
t.fillcolor("#0039a6")
t.begin_fill()
for i in range(1,4):
    t.left(90)
    t.fd(blue)
t.end_fill()

#星
t.left(90)
t.pencolor("white")
t.fillcolor("white")
t.penup()
t.goto(-w /2 + w / 2 /3 - 50, h / 2 - blue / 2 + 25)
t.pendown()
t.begin_fill()
for _ in range(5):
   t.forward(100)
   t.right(144)
t.end_fill()

t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="智利国旗.eps") #将图片保存下来

turtle.done()