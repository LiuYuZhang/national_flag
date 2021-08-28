"""
拉脱维亚国旗
拉脱维亚共和国（拉脱维亚语：Latvijas Republika），简称拉脱维亚。国名源自民族语，意为“铠甲”、“金属制的服装”，是一个位于欧洲东北部的议会共和制国家。
拉脱维亚国旗呈横长方形，长与宽之比约为2：1。自上而下由红、白、红三个平行的横宽条组成
"""

import turtle

w = 900
h = 450
h_m = h/5
turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)
t.hideturtle()

#顶部红色
t.pencolor("#9e3039")
t.fillcolor("#9e3039")
t.begin_fill()
t.penup()
t.goto(0, h_m / 2)
t.pendown()
t.forward(w/2)
t.left(90)
t.forward(2*h_m)
t.left(90)
t.forward(w)
t.left(90)
t.forward(2*h_m)
t.left(90)
t.forward(w/2)
t.end_fill()


#中间白色
t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.penup()
t.goto(0,-h_m / 2)
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

#底部红色
t.pencolor("#9e3039")
t.fillcolor("#9e3039")
t.begin_fill()
t.penup()
t.goto(0,- 2 * h_m - h_m / 2)
t.pendown()
t.forward(w/2)
t.left(90)
t.forward(2* h_m)
t.left(90)
t.forward(w)
t.left(90)
t.forward(2*h_m)
t.left(90)
t.forward(w/2)
t.end_fill()

ts = t.getscreen()
ts.getcanvas().postscript(file="拉脱维亚国旗.eps") #将图片保存下来

turtle.done()