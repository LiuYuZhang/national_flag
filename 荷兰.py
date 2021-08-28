"""
荷兰国旗
荷兰王国（The Kingdom of the Netherlands），简称“荷兰”。是由荷兰、阿鲁巴、库拉索和荷属圣马丁4个构成国组成的君主立宪制的复合国。荷兰国旗呈长方形，长与宽之比为3∶2。
自上而下由红、白、蓝三个平行相等的横长方形相连而成。蓝色表示国家面临海洋，象征人民的幸福；白色象征自由、平等、民主。还代表人民纯朴的性格特征；红色代表革命胜利。
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

#顶部红色
t.pencolor("#ae1c28")
t.fillcolor("#ae1c28")
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
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
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
t.pencolor("#21468b")
t.fillcolor("#21468b")
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
ts.getcanvas().postscript(file="荷兰国旗.eps") #将图片保存下来

turtle.done()