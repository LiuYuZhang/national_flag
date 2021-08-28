"""
中非共和国国旗
中非国旗呈长方形，长与宽之比为5∶3。旗面由四个平行相等的横长方形和一个竖长方形构成。横长方形自上而下依次为蓝、白、绿、黄四色，红色竖长方形将旗面分成左右相等的两部分。
旗面左上角有一颗黄色五角星。蓝、白、红三色与法国国旗颜色相同，表示中非与法国的历史关系，还象征和平与牺牲精神；绿色象征森林；黄色象征热带草原和沙漠。
五角星是指引中非人民奔向未来的灿烂之星。
"""

import turtle

width = 900
height = 540
turtle.screensize(width,height,"white")
turtle.setup(width=width,height=height)
item = height / 4

t = turtle.Turtle()
t.pensize(1)
t.speed(10)


#蓝
t.penup()
t.goto(0,height/2)
t.pendown()
t.pencolor("#003082")
t.fillcolor("#003082")
t.forward(width/2)
t.right(90)
t.begin_fill()
t.forward(item)
t.right(90)
t.forward(width)
t.right(90)
t.forward(item)
t.right(90)
t.forward(width / 2)
t.end_fill()

#白
t.penup()
t.goto(width / 2,item)
t.right(90)
t.pendown()
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
t.begin_fill()
t.fd(item)
t.right(90)
t.fd(width)
t.right(90)
t.fd(item)
t.right(90)
t.fd(width)
t.end_fill()

#绿
t.penup()
t.goto(width / 2,0)
t.right(90)
t.pendown()
t.pencolor("#299727")
t.fillcolor("#299727")
t.begin_fill()
t.fd(item)
t.right(90)
t.fd(width)
t.right(90)
t.fd(item)
t.right(90)
t.fd(width)
t.end_fill()


# #黄
t.penup()
t.goto(width / 2,-item)
t.right(90)
t.pendown()
t.pencolor("#fece00")
t.fillcolor("#fece00")
t.begin_fill()
t.fd(item)
t.right(90)
t.fd(width)
t.right(90)
t.fd(item)
t.right(90)
t.fd(width)
t.end_fill()


#红
t.penup()
t.goto(-item/ 2,height / 2)
t.pendown()
t.pencolor("#d21033")
t.fillcolor("#d21033")
t.begin_fill()
t.fd(item)
t.right(90)
t.fd(height)
t.right(90)
t.fd(item)
t.right(90)
t.fd(height)
t.right(90)
t.fd(item)
t.end_fill()

#星
t.penup()
t.goto(- width /2 * 0.86 ,height / 2 - item * 0.8 / 2)
t.pendown()

t.pencolor("#fece00")
t.fillcolor("#fece00")
t.begin_fill()
for _ in range(5):
   t.forward(item * 0.8)
   t.right(144)
t.end_fill()

t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="中非共和国国旗.eps") #将图片保存下来

turtle.done()
