"""
立陶宛国旗
立陶宛共和国（Republic of Lithuania），简称立陶宛，位于波罗的海东岸，与北方的拉脱维亚和爱沙尼亚，并称为波罗的海三国，东南邻白俄罗斯，西南是俄罗斯的加里宁格勒州和波兰，首都维尔纽斯。
立陶宛国旗呈横长方形，长与宽之比为5:3。由三个平行的横长条组成，自上而下分别为黄、绿、红三色。立陶宛于1918年宣布独立，建立资产阶级共和国，采用黄、绿、红三色旗作为国旗。
1940年成为原苏联的一个加盟共和国，采用左上角有黄色五角星及镰刀、铁锤图案，下部有白色窄条和绿色宽条的红旗作为国旗。
1990年宣布独立，采用上述三色旗为国旗。2004年7月8日国旗的长宽比例从2:1变成5:3
"""

import turtle

w = 900
h = 600
h_m = h/5
turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)
t.hideturtle()

#顶部黄色
t.pencolor("#fcb913")
t.fillcolor("#fcb913")
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


#中间绿色
t.pencolor("#006a44")
t.fillcolor("#006a44")
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

#底部红色
t.pencolor("#c2272d")
t.fillcolor("#c2272d")
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
ts.getcanvas().postscript(file="立陶宛国旗.eps") #将图片保存下来

turtle.done()