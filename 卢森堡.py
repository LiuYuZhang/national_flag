"""
卢森堡国旗
卢森堡大公国，简称卢森堡，位于欧洲西北部，被邻国法国、德国和比利时包围，是一个内陆国，也是现今欧洲大陆仅存的大公国，首都卢森堡市。因国土小、古堡多，又有“袖珍王国”、“千堡之国”的称呼。
卢森堡国旗呈长方形，长宽之比为5:3或2:1。旗面由三个平行相等的横长方形组成，自上而下分别为红、白、浅蓝三色。
红色象征着热烈和勇敢的国民性格，还象征在争取国家独立和民族解放斗争中牺牲烈士的鲜血；白色象征人民的纯朴和对和平的追求；蓝色代表蓝天，意味着人民获得了光明和幸福。
三色联在一起又象征平等、民主和自由。
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
t.pencolor("#d70103")
t.fillcolor("#d70103")
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
t.pencolor("#fefefe")
t.fillcolor("#fefefe")
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
t.pencolor("#00b6e8")
t.fillcolor("#00b6e8")
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
ts.getcanvas().postscript(file="卢森堡国旗.eps") #将图片保存下来

turtle.done()