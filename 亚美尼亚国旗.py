"""
 亚美尼亚国旗
 亚美尼亚共和国，简称亚美尼亚，是一个位于亚洲与欧洲交界处的外高加索地区的共和制国家。亚美尼亚国旗呈横长方形，长与宽之比为2：1。自上而下由红、蓝、橙三个平行且相等的横长方形组成。
 红色象征烈士的鲜血和国家革命的胜利，蓝色代表国家丰富的资源，橙色象征光明、幸福和希望。这是1918年成立的亚美尼亚第一共和国就采用的国旗。
 1920年至1991年，亚美尼亚曾是原苏联的一个加盟共和国，当时的国旗是在原苏联国旗的旗面中间加一个稍宽的蓝色横条。1991年宣布独立，正式恢复红、蓝、橙三色旗为国旗。
"""

import turtle

w = 900
h = 450
turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)
t.hideturtle()

#顶部红色
t.pencolor("#d90012")
t.fillcolor("#d90012")
t.begin_fill()
t.penup()
t.goto(0,h/3/2)
t.pendown()
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
t.pencolor("#0033a0")
t.fillcolor("#0033a0")
t.begin_fill()
t.penup()
t.goto(0,-h/3/2)
t.pendown()
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

#底部橙色
t.pencolor("#f2a800")
t.fillcolor("#f2a800")
t.begin_fill()
t.penup()
t.goto(0,-h/3-h/3/2)
t.pendown()
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

turtle.mainloop()
