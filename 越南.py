"""
越南国旗
越南社会主义共和国（Socialist Republic of Vietnam，Vietnam），简称“越南”，是亚洲的一个社会主义国家。越南的首都是河内，国歌为《进军歌》，越南国旗为长方形，红底中间有五角金星。
国旗自1955年11月30日开始采用。即通常说的金星红旗。长宽比例为3:2。
国旗旗地为红色，旗中心为一枚五角金星。红色象征革命和胜利，五角金星象征越南共产党对国家的领导，五星的五个角分别代表工人、农民、士兵、知识分子和青年。
"""

import turtle
from typing import ItemsView

w = 900
h = 600

turtle.screensize(w,h,"white")
turtle.setup(w,h)

#绿
t = turtle.Turtle()
t.pensize(1)
t.speed(10)

t.pencolor("#da251d")
t.fillcolor("#da251d")
t.penup()
t.goto(-w/2,0)
t.pendown()
t.begin_fill()
t.left(90)
t.forward(h/2)
t.right(90)
t.fd(w)
t.right(90)
t.fd(h)
t.right(90)
t.fd(w)
t.end_fill()



#星
t.right(180)
t.penup()
t.goto(-150,70)
t.pendown()
t.pencolor("#ffff00")
t.fillcolor("#ffff00")
t.begin_fill() 
for _ in range(5):
   t.forward(300)
   t.right(144)
t.end_fill() 

t.hideturtle()


ts = t.getscreen()
ts.getcanvas().postscript(file="越南国旗.eps") #将图片保存下来

turtle.done()

