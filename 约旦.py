"""
约旦国旗
约旦国旗 （阿拉伯语：علم الأردن‎）源于阿拉伯大起义。国旗呈横长方形，长与宽之比为2：1。
由泛阿拉伯颜色：红 （哈希姆王朝）、绿 （绿衣大食）、黑 （黑衣大食）、白 （白衣大食）组成。
靠旗杆一侧为红色等腰三角形，内有一颗白色七角星。白色七角星象征古兰经。 [1] 
"""

import turtle
import math

w = 900
h = 450
h_m = h/3
turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)



#黑
t.pencolor("#000000")
t.fillcolor("#000000")

t.penup()
t.goto(w/ 2,h/2)
t.pendown()
t.begin_fill()
for i in range(1,4):       
       t.right(90)
       if i % 2 == 0:
              t.fd(w)
       else:
              t.fd(h_m)
       
t.end_fill()



#白
t.pencolor("white")
t.fillcolor("white")
t.penup()
t.home()
t.goto(w/ 2,h_m / 2)
t.pendown()
t.begin_fill()
for i in range(1,4):
       t.right(90)
       if i % 2 == 0:
              t.fd(w)              
       else:
              t.fd(h_m)
              
t.end_fill()

#绿
t.pencolor("#007a3d")
t.fillcolor("#007a3d")
t.penup()
t.home()
t.goto(w/ 2, -h_m /2)
t.pendown()
t.begin_fill()
for i in range(1,4):
       t.right(90)
       if i % 2 == 0:
              t.fd(w)
       else:
              t.fd(h_m)
t.end_fill()




#红色三角形
t.right(270)
t.penup()
t.home()
t.goto(-w/2,h/2)
t.pendown()
t.pencolor("#d21034")
t.fillcolor("#d21034")
t.begin_fill()
t.right(30)
t.fd(h)
t.right(120)
t.fd(h)
t.end_fill()


#星
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
t.penup()
t.home()
t.goto(-340,20)
t.right(180/7)
t.pendown()
t.begin_fill()
for i in range(7):
       t.fd(50)
       t.right(180-180/7)
t.end_fill()

t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="约旦国旗.eps") #将图片保存下来

turtle.done()