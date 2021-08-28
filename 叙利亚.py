"""
叙利亚国旗
阿拉伯叙利亚共和国（The Syrian Arab Republic）国旗呈长方形，长与宽之比为3：2。旗面自上而下由红、白、黑三个平行的横长方形相连构成，在白色部分中有两个大小一样的绿色五角星。
红色象征勇敢，白色象征纯洁和宽容，黑色是穆罕默德已赢得胜利的象征，绿色是穆罕默德的子孙所喜爱的颜色，五角星象征阿拉伯革命。
"""

import turtle

w = 900
h = 600
h_m = h/3
turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)

#红
t.pencolor("#ce1127")
t.fillcolor("#ce1127")
t.begin_fill()
t.penup()
t.goto(0,h_m/2)
t.pendown()
t.forward(w/2)
t.left(90)
t.forward(h_m)
t.left(90)
t.forward(w)
t.left(90)
t.forward(h_m)
t.left(90)
t.forward(w/2)
t.end_fill()


#白
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
t.begin_fill()
t.penup()
t.goto(0,-h_m/2)
t.pendown()
t.forward(w/2)
t.left(90)
t.forward(h_m)
t.left(90)
t.forward(w)
t.left(90)
t.forward(h_m)
t.left(90)
t.forward(w/2)
t.end_fill()

#黑
t.pencolor("#000000")
t.fillcolor("#000000")
t.begin_fill()
t.penup()
t.goto(0,-h_m-h_m/2)
t.pendown()
t.forward(w/2)
t.left(90)
t.forward(h_m)
t.left(90)
t.forward(w)
t.left(90)
t.forward(h_m)
t.left(90)
t.forward(w/2)
t.end_fill()


#星
x = h_m * 0.8
t.pencolor("#007a3d")
t.fillcolor("#007a3d")
t.penup()
t.goto(100,20)
t.pendown()
t.begin_fill()
for _ in range(5):
   t.forward(x)
   t.right(144)
t.end_fill()

t.penup()
t.goto(-220,20)
t.pendown()
t.begin_fill()
for _ in range(5):
   t.forward(x)
   t.right(144)
t.end_fill()

t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="叙利亚国旗.eps") #将图片保存下来

turtle.done()