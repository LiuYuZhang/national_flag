"""
贝宁共和国国旗
贝宁共和国（The Republic of Benin），简称贝宁，是一个位于西非中南部的国家，首都波多诺伏。
贝宁国旗呈长方形，长宽之比约为3：2。旗面左侧为一绿色竖长方形，右侧为上黄下红两个平行相等的横长方形。
这面国旗于1959年制定，在1975年至1990年之间曾被弃用。红黄绿三色是非洲人民喜爱的，被称为“泛非洲颜色”，象征非洲人的团结。
红色象征土地或祖先的鲜血；黄色象征平原；绿色象征棕榈树。
"""

import turtle

w = 900
h = 600
item = w / 15 *6
item2 = w / 15 *9

turtle.screensize(w,h,"white")
turtle.setup(width=w,height=h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)
#t.hideturtle()


#绿
t.penup()
t.goto(-w /2  ,0)
t.pendown()
t.pencolor("#008751")
t.fillcolor("#008751")
t.begin_fill()
t.left(90)
t.forward(h/2)
t.right(90)
t.fd(item)
t.right(90)
t.fd(h)
t.right(90)
t.fd(item)
t.end_fill()


#红
t.right(180)
t.pencolor("#e8112d")
t.fillcolor("#e8112d")
t.begin_fill()
t.forward(w)
t.left(90)
t.forward(h / 2)
t.left(90)
t.forward(item2)
t.left(90)
t.forward(h/2)
t.end_fill()


#黄
t.right(180)
t.forward(h/2)
t.pencolor("#fcd116")
t.fillcolor("#fcd116")
t.begin_fill()
t.forward(h/2)
t.right(90)
t.forward(item2)
t.right(90)
t.forward(h /2)
t.end_fill()

ts = t.getscreen()
ts.getcanvas().postscript(file="贝宁共和国国旗.eps") #将图片保存下来

turtle.done()
