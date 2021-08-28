"""
 马尔代夫国旗
 马尔代夫共和国国旗是由红、绿和白三色组成,长与宽之比3：2。旗地为绿色长方形，四周为宽度占全旗宽度1/4的红边，绿色长方形正中为一牙白色新月。
 红色象征为国献身的民族英雄的鲜血，绿色表示生命、进步和繁荣，白色新月表示和平、安宁和人民对伊斯兰教的信仰。古老的国旗原为红旗，1910年增加绿色长方形和新月。
"""

import turtle

w,h  = 900,600
item = w / 6
turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)


#红
t.pencolor("#d21033")
t.fillcolor("#d21033")
t.penup()
t.goto(-w / 2, h / 2)
t.pendown()
t.begin_fill()
for i in range(4):
    if i % 2 == 0:
        t.fd(w)
    else:
        t.fd(h)
    t.right(90)
t.end_fill()


#绿
t.pencolor("#017e3a")
t.fillcolor("#017e3a")
t.penup()
t.goto(-w / 2 + item, h / 2 - item)
t.pendown()
t.begin_fill()
for i in range(4):
    if i % 2 == 0:
        t.fd(item * 4)
    else:
        t.fd(item * 2)
    t.rt(90)
t.end_fill()


#将绿色再分为5份
#月
t.penup()
t.goto(-item / 2 + (w / 5 / 2),-h/4/2)
t.pendown()
t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.circle(h / 4 / 2,360)
t.end_fill()

#用另一个圆覆盖
t.pencolor("#017e3a")
t.fillcolor("#017e3a")
t.penup()
t.home()
t.sety(-h/4/2)
t.setx(h/4/4)
t.pendown()

t.begin_fill()
t.circle(h / 4 / 2,-360)
t.end_fill()
t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="马尔代夫国旗.eps") #将图片保存下来

turtle.mainloop()
