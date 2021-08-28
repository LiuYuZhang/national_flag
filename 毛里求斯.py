"""
毛里求斯国旗
毛里求斯共和国（The Republic of Mauritius），简称毛里求斯，为非洲东部一岛国，位于印度洋西南方。作为火山岛国，毛里求斯四周被珊瑚礁环绕，岛上地貌千姿百态，首都路易港。
毛里求斯国旗启用于1968年3月12日。国旗长宽之比为3：2。由红、蓝、黄、绿四个平行相等的长方形构成。
红色象征为独立自由而斗争，蓝色表示毛里求斯位于蓝色的南印度洋，黄色象征独立的光芒照耀岛国，绿色表示国家的农业和四季常青。
"""

import turtle

w = 900
h = 600
item = h/4
turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)
t.hideturtle()

#红色
t.pencolor("#ea2839")
t.fillcolor("#ea2839")
t.begin_fill()
t.penup()
t.goto(0,item)
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


#蓝色
t.pencolor("#1a206d")
t.fillcolor("#1a206d")
t.begin_fill()
t.penup()
t.goto(0,0)
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

#黄色
t.pencolor("#ffd500")
t.fillcolor("#ffd500")
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

#绿色
t.pencolor("#00a551")
t.fillcolor("#00a551")
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
ts.getcanvas().postscript(file="毛里求斯国旗.eps") #将图片保存下来

turtle.done()