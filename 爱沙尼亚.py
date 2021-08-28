"""
爱沙尼亚国旗
爱沙尼亚共和国（Republic of Estonia），简称爱沙尼亚，与南方的拉脱维亚和立陶宛并称为波罗的海三国。爱沙尼亚旗（爱沙尼亚语：Eesti lipp）呈长方形，长与宽之比为11:7。
旗面由三个平行相等的横长方形相连组成，自上而下分别为蓝、黑、白三色。旗的正常大小为105厘米×165厘米。
在爱沙尼亚语中，国旗通常叫做“sinimustvalge”（意思为“蓝—黑—白”），是以色条的分布从上往下称呼的。
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

#顶部蓝色
t.pencolor("#0072ce")
t.fillcolor("#0072ce")
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


#中间黑色
t.pencolor("#000000")
t.fillcolor("#000000")
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

#底部白色
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
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
ts.getcanvas().postscript(file="爱沙尼亚国旗.eps") #将图片保存下来

turtle.done()