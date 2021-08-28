"""
波兰国旗
波兰共和国（The Republic Of Poland），简称波兰(Poland)，是一个位于中欧，由16个省组成的民主共和制国家。波兰国旗呈横长方形，长与宽之比约为8∶5。
旗面由上白下红两个平行相等的横长方形构成。
白色不仅象征古老传说中的白鹰，而且还象征着纯洁，表达出波兰人民渴望自由、和平、民主、幸福的美好愿望；红色象征热血，也象征着革命斗争取得胜利。
"""

import turtle

w = 900
h = w/8*5
turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)
t.hideturtle()

#顶部白色
t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.forward(w/2)
t.left(90)
t.forward(h/2)
t.left(90)
t.forward(w)
t.left(90)
t.forward(h/2)
t.left(90)
t.forward(w/2)
t.end_fill()


#底部红色
t.pencolor("#dc143c")
t.fillcolor("#dc143c")
t.begin_fill()
t.penup()
t.goto(0,-h/2)
t.pendown()
t.forward(w/2)
t.left(90)
t.forward(h/2)
t.left(90)
t.forward(w)
t.left(90)
t.forward(h/2)
t.left(90)
t.forward(w/2)
t.end_fill()


ts = t.getscreen()
ts.getcanvas().postscript(file="波兰国旗.eps") #将图片保存下来

turtle.done()