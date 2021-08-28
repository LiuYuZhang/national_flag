"""
匈牙利国旗
匈牙利，是一个位于欧洲中部的内陆国家，首都为布达佩斯，官方语言为匈牙利语 。匈牙利国旗呈长方形，长与宽之比为3∶2。
自上而下由红、白、绿三个平行相等的横长方形相连而成。红色象征爱国者的热血，还象征国家的独立和主权；
白色象征和平，代表人民追求自由和光明的美好愿望；绿色象征着匈牙利的繁荣昌盛，象征人民对未来充满信心和希望。
"""

import turtle

w = 900
h = 400
turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)
t.hideturtle()

#顶部红色
t.pencolor("#cd2a3e")
t.fillcolor("#cd2a3e")
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
t.pencolor("white")
t.fillcolor("white")
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

#底部绿色
t.pencolor("#436f4d")
t.fillcolor("#436f4d")
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
ts.getcanvas().postscript(file="匈牙利国旗.eps") #将图片保存下来

turtle.done()