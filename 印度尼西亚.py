"""
印度尼西亚国旗
印度尼西亚共和国（Republic of Indonesia），简称印尼（Indonesia）。是东南亚国家，首都为雅加达，国歌《伟大的印度尼西亚》，印度尼西亚国旗（Sang Merah Putih）别称“荣耀红白”，
是一面由红白两色横带组成的旗帜。长宽比例为3:2。这面旗帜是基于13世纪满者伯夷的旗帜设计的。1945年8月17日首次升起。此后没有更改过。
旗帜的设计很简单，是两条一样宽的横带，上面的那横带是红色的，下面的横带是白色的。
红色象征勇敢和正义，还象征印度尼西亚独立以后的繁荣昌盛；白色象征自由、公正、纯洁，还表达了印尼人民反对侵略、爱好和平的美好愿望。
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
t.pencolor("#ce1126")
t.fillcolor("#ce1126")
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


#底部白色
t.pencolor("white")
t.fillcolor("white")
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
ts.getcanvas().postscript(file="印度尼西亚国旗.eps") #将图片保存下来

turtle.done()