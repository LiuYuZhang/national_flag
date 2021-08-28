"""
 加蓬国旗
 加蓬共和国（The Gabonese Republic），位于非洲中部西海岸，横跨赤道线。加蓬的首都为利伯维尔，加蓬国旗呈长方形，长宽之比为4:3。
 自上而下由绿、黄、蓝三个平行的横长方形组成。绿色象征丰富的森林资源，加蓬号称“木材之国”、“绿金之国”；黄色象征阳光黄色也代表丰富的矿产资源；蓝色象征海洋。
"""

import turtle

w = 900
h = 675
turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)
t.hideturtle()

#顶部绿色
t.pencolor("#009e60")
t.fillcolor("#009e60")
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


#中间黄色
t.pencolor("#fcd116")
t.fillcolor("#fcd116")
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
t.pencolor("#3a75c4")
t.fillcolor("#3a75c4")
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
ts.getcanvas().postscript(file="加蓬国旗.eps") #将图片保存下来

turtle.mainloop()
