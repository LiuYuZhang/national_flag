"""
吉布提国旗
吉布提国旗
吉布提共和国（The Republic of Djibouti），简称吉布提，地处非洲东北部亚丁湾西岸，首都吉布提市。吉布提国旗呈长方形，长与宽之比约为9∶5。
靠旗杆一侧为一个白色等边三角形，边长与旗宽相等；右侧为两个相等的直角梯形，上方为天蓝色，下方为绿色。白色三角形正中有一颗红色五角星。
天蓝色代表海洋和天空，绿色象征土地和希望，白色象征和平，红五角星代表人民的希望和斗争的方向。整个国旗图案的中心思想是“团结、平等、和平”。
"""

import turtle
import math

w = 900
h = 500
item = h / 2
c = math.sqrt((math.pow(item,2) + math.pow(w/2,2))) #三角形边长
turtle.screensize(w,h,"white")
turtle.setup(w,h)


t = turtle.Turtle()
t.pensize(1)
t.speed(10)

#白
t.pencolor("#6ab2e7")
t.fillcolor("#6ab2e7")
t.begin_fill()
t.forward(w/2)
t.left(90)
t.forward(item)
t.left(90)
t.forward(w)
t.left(90)
t.forward(item)
t.left(90)
t.forward(w/2)
t.end_fill()


#红
t.pencolor("#12ad2b")
t.fillcolor("#12ad2b")
t.begin_fill()
t.forward(w/2)
t.right(90)
t.forward(item)
t.right(90)
t.forward(w)
t.right(90)
t.forward(item)
t.right(90)
t.forward(w/2)
t.end_fill()


#三角
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
t.begin_fill()
t.left(151)
t.forward(c)
t.left(119)
t.forward(h)
t.end_fill()

#星
t.left(90)
t.penup()
t.goto(-w / 2 / 2 - 80,16)
t.pendown()

t.pencolor("#d7141a")
t.fillcolor("#d7141a")
t.begin_fill()
for _ in range(5):
   t.forward(80)
   t.right(144)
t.end_fill()

t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="吉布提国旗.eps") #将图片保存下来

turtle.done()