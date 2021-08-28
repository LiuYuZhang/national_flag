"""
 保加利亚国旗
 保加利亚共和国，简称保加利亚。是欧洲东南部巴尔干半岛东南部的一个国家。保加利亚国旗呈长方形，长宽之比为5:3。
 旗面自上而下由白、绿、红三个平行相等的横长方形组成。白色象征人民热爱和平与自由，绿色象征农业和国家的主要财富，红色象征勇士的鲜血。
 白、红两色是古老的波希米亚王国的传统色。这面国旗采用于1990年9月22日，原版三色旗则采用于1878年。
"""

import turtle

w = 900
h = 540
turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)
t.hideturtle()

#顶部白色
t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.penup()
t.goto(0,h/3/2)
t.pendown()
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


#中间绿色
t.pencolor("#00966e")
t.fillcolor("#00966e")
t.begin_fill()
t.penup()
t.goto(0,-h/3/2)
t.pendown()
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

#底部红色
t.pencolor("#d62612")
t.fillcolor("#d62612")
t.begin_fill()
t.penup()
t.goto(0,-h/3-h/3/2)
t.pendown()
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

ts = t.getscreen()
ts.getcanvas().postscript(file="保加利亚国旗.eps") #将图片保存下来

turtle.mainloop()
