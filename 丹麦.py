"""
丹麦国旗    
丹麦王国（丹麦语：Kongeriget Danmark，旧译为“嗹(lián)国”、“嗹马”），简称丹麦，北欧五国之一，是一个君主立宪制国家，拥有两个自治领地，法罗群岛和格陵兰。
丹麦国旗是现今仍在使用的国旗之中最为古老、历史最为悠久的一面，被称为“丹麦人的力量”。呈长方形，长与宽之比为37∶28。旗地为红色，旗面上有白色十字形图案，稍偏左侧。
据丹麦史诗记载，公元1219年丹麦国王瓦尔德玛·维克托里斯（也称胜利王）率军对爱沙尼亚异教徒征战。
6月15日隆达尼斯战斗中，丹军陷入困境。突然，一面带有白色十字的红旗从天而降，并伴随着一个响亮的声音：“抓住这面旗帜就是胜利！”在这面旗帜的鼓舞下，丹麦军奋勇作战，转败为胜。
此后白色十字红旗就成为丹麦王国的国旗。每年6月15日，丹麦都要庆祝“国旗日”即“瓦尔德玛日”。
"""

import turtle

w = 900
h = 682
item = 112

turtle.screensize(w,h,"white")
turtle.setup(w,h)
t = turtle.Turtle()
t.speed(10)
t.pensize(1)
t.hideturtle()


#底色框
t.pencolor("#d00c33")
t.fillcolor("#d00c33")
t.penup()
t.goto(-w/2,-h / 2)
t.pendown()
t.begin_fill()
t.forward(w)
t.left(90)
t.forward(h)
t.left(90)
t.forward(w)
t.end_fill()

#横向白色块
t.penup()
t.pencolor("white")
t.fillcolor("white")
t.goto(-w/2,-item/2)
t.pendown()
t.right(180)
t.begin_fill()
t.forward(w)
t.left(90)
t.forward(item)
t.left(90)
t.forward(w)
t.end_fill()


#纵向红色块
t.penup()
t.goto(-item/2,h/2)
t.pendown()
t.begin_fill()
t.forward(item)
t.left(90)
t.forward(h)
t.left(90)
t.forward(item)
t.left(90)
t.end_fill()

ts = t.getscreen()
ts.getcanvas().postscript(file="丹麦国旗.eps") #将图片保存下来

turtle.done()

