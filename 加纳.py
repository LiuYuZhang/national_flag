"""
加纳国旗
加纳共和国（The Republic of Ghana），是非洲西部的一个国家，位于非洲西部，首都阿克拉。加纳国旗呈长方形，长与宽之比为3:2。
自上而下由红、黄、绿三个平行相等的横长方形组成，黄色部分中间是一颗黑色五角星。
红色象征为了国家独立而牺牲烈士的鲜血；黄色象征国家丰富的矿藏和资源；也代表加纳原来的国名“黄金海岸”；绿色象征森林和农业；黑色五角星象征非洲自由的北极星。
"""

import turtle

w = 900
h = 600
turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)

#红
t.pencolor("#ce1126")
t.fillcolor("#ce1126")
t.begin_fill()
t.penup()
t.goto(0,h/3/2)
t.pendown()
t.forward(w/2)
t.left(90)
t.forward(h/3)
t.left(90)
t.forward(w)
t.left(90)
t.forward(h/3)
t.left(90)
t.forward(w/2)
t.end_fill()


#黄
t.pencolor("#fcd116")
t.fillcolor("#fcd116")
t.begin_fill()
t.penup()
t.goto(0,-h/3/2)
t.pendown()
t.forward(w/2)
t.left(90)
t.forward(h/3)
t.left(90)
t.forward(w)
t.left(90)
t.forward(h/3)
t.left(90)
t.forward(w/2)
t.end_fill()

#绿
t.pencolor("#006b3f")
t.fillcolor("#006b3f")
t.begin_fill()
t.penup()
t.goto(0,-h/3-h/3/2)
t.pendown()
t.forward(w/2)
t.left(90)
t.forward(h/3)
t.left(90)
t.forward(w)
t.left(90)
t.forward(h/3)
t.left(90)
t.forward(w/2)
t.end_fill()

#星
t.pencolor("#000000")
t.fillcolor("#000000")
t.penup()
t.goto(-50,25)
t.pendown()
t.begin_fill()
for _ in range(5):
   t.forward(100)
   t.right(144)
t.end_fill()

t.hideturtle()
ts = t.getscreen()
ts.getcanvas().postscript(file="加纳国旗.eps") #将图片保存下来

turtle.done()