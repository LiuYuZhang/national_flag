"""
阿拉伯联合酋长国国旗
阿拉伯联合酋长国，简称“阿联酋”，是位于亚洲西南部阿拉伯半岛东部的西亚国家。阿拉伯联合酋长国国旗呈长方形，长与宽之比为2比1。
由红、绿、白、黑四色组成，这四色是泛阿拉伯颜色，代表穆罕默德后代的几个王朝。旗面靠旗杆一侧为红色竖长方形，右侧是三个平行相等的横长方形，自上而下分别为绿、白、黑三色。
红色象征祖国，绿色象征牧场，白色象征祖国的成就，黑色象征战斗。
"""

import turtle

w = 900
h = 450
h_m = h/3
turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)

#绿
t.pencolor("#00732e")
t.fillcolor("#00732e")
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

#红
t.penup()
t.goto(-w/2,h/2)
t.pendown()
t.pencolor("#fe0000")
t.fillcolor("#fe0000")
t.begin_fill()
for i in range(1,4):
    if i % 2 == 0:
        t.fd(h)
    else:
        t.fd(200)
    t.right(90)

t.end_fill()


ts = t.getscreen()
ts.getcanvas().postscript(file="阿拉伯联合酋长国国旗.eps") #将图片保存下来

turtle.done()