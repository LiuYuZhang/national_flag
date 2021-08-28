"""
哥伦比亚国旗
哥伦比亚共和国（The Republic of Colombia），简称“哥伦比亚”，是位于南美洲北部的海陆兼备国，首都波哥大 。
哥伦比亚共和国国旗启用于1861年11月26日，国旗呈长方形，长与宽之比约为3:2。自上而下由黄、蓝、红三个平行横长方形相连而成，黄色部分占旗面的一半，蓝色、红色各占旗面的1/4。
黄色代表着土壤的丰富和财富，也代表着主权，和谐与正义；蓝色代表海洋，哥伦比亚是沿海的两个海洋，使国民团结到其他城镇进行产品交换。红色代表鲜血，意味着爱、力量和进步。
"""

import turtle

w = 900
h = 600
item = h / 4
turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)
t.hideturtle()

#顶部黄色
t.pencolor("#fcd116")
t.fillcolor("#fcd116")
t.begin_fill()
t.penup()
t.goto(0,0)
t.pendown()
t.forward(w/2)
t.left(90)
t.forward(item * 2 )
t.left(90)
t.forward(w)
t.left(90)
t.forward(item * 2)
t.left(90)
t.forward(w/2)
t.end_fill()


#中间蓝色
t.pencolor("#003893")
t.fillcolor("#003893")
t.begin_fill()
t.penup()
t.goto(0,-item)
t.pendown()
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

#底部红色
t.pencolor("#ce1126")
t.fillcolor("#ce1126")
t.begin_fill()
t.penup()
t.goto(0,-2 * item)
t.pendown()
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
ts = t.getscreen()
ts.getcanvas().postscript(file="哥伦比亚国旗.eps") #将图片保存下来

turtle.done()