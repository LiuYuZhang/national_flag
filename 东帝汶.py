"""
东帝汶民主共和国国旗
黄色象征殖民主义者的痕迹；黑色象征需要克服的落后文化；红色象征民族解放斗争；白色象征和平。2002年5月20日独立日正式启用这面国旗。
中心图案源自东帝汶独立革命阵线旗帜，象征为取得独立而进行的不懈斗争。
"""

import turtle

w,h = 900,450

turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)

#红
t.pencolor("#db241e")
t.fillcolor("#db241e")
t.penup()
t.goto(w/2,h/2)
t.pendown()
t.begin_fill()
for i in range(4):
    t.right(90)
    if i % 2 == 0:
        t.fd(h)
    else:
        t.fd(w)
t.end_fill()

#黄
t.pencolor("#fec726")
t.fillcolor("#fec726")
t.penup()
t.right(90)
t.goto(-w/2,h/2)
t.pendown()
t.begin_fill()
t.fd(h/2)
t.left(90)
t.fd(w/2)
t.end_fill()

t.penup()
t.goto(-w/2,-h /2)
t.pendown()
t.begin_fill()
t.left(90)
t.fd(h/2)
t.right(90)
t.fd(w/2)
t.end_fill()


#黑
c = w * 0.33333
t.pencolor("#000000")
t.fillcolor("#000000")
t.penup()
t.right(90)
t.goto(-w/2,h/2)
t.pendown()
t.begin_fill()
t.fd(h/2)
t.left(90)
t.fd(c)
t.end_fill()

t.penup()
t.goto(-w/2,-h /2)
t.pendown()
t.begin_fill()
t.left(90)
t.fd(h/2)
t.right(90)
t.fd(c)
t.end_fill()


#白
x = w / 6
t.pencolor("white")
t.fillcolor("white")
t.penup()
t.home()
t.goto(-w/2 + x / 6,0)
t.left(23)
t.pendown()
t.begin_fill()
for _ in range(5):
   t.forward(x)
   t.right(144)
t.end_fill()

t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="东帝汶国旗.eps") #将图片保存下来

turtle.done()