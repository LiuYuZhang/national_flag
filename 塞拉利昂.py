"""
塞拉利昂国旗
塞拉利昂共和国（The Republic of Sierra Leone），简称塞拉利昂，是世界最不发达国家之一。位于西非大西洋岸，北部及东部被几内亚包围、东南与利比里亚接壤，首都弗里敦。
塞拉利昂国旗启用于1961年4月27日。国旗长度比例为3：2。国旗由三个平行相等的横长方形组成，自上而下依次为绿、白、蓝三色。
绿色象征农业，还代表国家的自然资源和山脉；白色象征国家的统一和人民对正义的追求；蓝色象征海洋和希望，希望塞拉利昂的天然良港对世界和平作出贡献。
"""

import turtle

w = 900
h = 600
turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)
t.hideturtle()

#顶部绿色
t.pencolor("#1eb53a")
t.fillcolor("#1eb53a")
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


#中间白色
t.pencolor("white")
t.fillcolor("white")
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

#底部蓝色
t.pencolor("#0072c6")
t.fillcolor("#0072c6")
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
ts = t.getscreen()
ts.getcanvas().postscript(file="塞拉利昂国旗.eps") #将图片保存下来

turtle.done()