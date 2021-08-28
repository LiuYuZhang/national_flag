"""
俄罗斯国旗
俄罗斯联邦（Russian Federation），又称俄罗斯（Russia）、俄联邦、俄国。是由22个自治共和国、46个州、9个边疆区、4个自治区、1个自治州、3个联邦直辖市组成的联邦共和立宪制国家。
俄罗斯国旗为白、蓝、红三色旗。国徽主体为双头鹰图案。俄罗斯位于欧亚大陆北部，地跨欧亚两大洲，是世界上面积最大的国家。
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

#顶部白色
t.pencolor("white")
t.fillcolor("white")
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


#中间蓝色
t.pencolor("#0039a6")
t.fillcolor("#0039a6")
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
t.pencolor("#d52b1e")
t.fillcolor("#d52b1e")
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
ts.getcanvas().postscript(file="俄罗斯国旗.eps") #将图片保存下来

turtle.done()