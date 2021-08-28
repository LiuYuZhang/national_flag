"""
巴拉马国旗
巴拿马国旗是代表中美洲南端巴拿马共和国政府的合法旗帜。这面旗帜也是巴拿马共和国境内最为人知的国家象征。
巴拿马国旗是一面分为4个部位的2:3比例长方形：左上角为白底与五角海蓝星；左下角为海蓝底；右上角为红底；右下角为白底与五角红星。
"""

import turtle

w = 900
h = 600
w_1_2 = w / 2 #宽度1/2
h_1_2 = h / 2 #高度1/2
turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)

#上红
t.pencolor("#d21033")
t.fillcolor("#d21033")
t.begin_fill()
t.forward(w_1_2)
t.left(90)
t.forward(h_1_2)
t.left(90)
t.forward(w_1_2)
t.left(90)
t.forward(h_1_2)
t.left(90)
t.forward(w_1_2)
t.end_fill()


#上白
t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.penup()
t.goto(0,0)
t.left(90)
t.forward(h_1_2)
t.left(90)
t.forward(w_1_2)
t.left(90)
t.forward(h_1_2)
t.left(90)
t.forward(w_1_2)
t.end_fill()

#下蓝
t.left(180)
t.pencolor("#0067c6")
t.fillcolor("#0067c6")
t.begin_fill()
t.forward(w_1_2)
t.left(90)
t.forward(h_1_2)
t.left(90)
t.fd(w_1_2)
t.left(90)
t.fd(h_1_2)
t.end_fill()


#下白
t.right(90)
t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.forward(w_1_2)
t.right(90)
t.forward(h_1_2)
t.right(90)
t.fd(w_1_2)
t.end_fill()

#上星
t.right(180)
x = 100
t.pencolor("#0073cf")
t.fillcolor("#0073cf")
t.penup()
t.goto(-w_1_2 / 2  - 50 ,h_1_2 / 2 + 30)
t.pendown()
t.begin_fill()
for _ in range(5):
   t.forward(x)
   t.right(144)
t.end_fill()


#下星
x = 100
t.pencolor("#d21033")
t.fillcolor("#d21033")
t.penup()
t.goto(w_1_2 / 2  - 50 , - h_1_2 / 2 + 30)
t.pendown()
t.begin_fill()
for _ in range(5):
   t.forward(x)
   t.right(144)
t.end_fill()

t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="洪都拉斯国旗.eps") #将图片保存下来

turtle.done()