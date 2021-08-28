"""
多哥鲜国旗
多哥国旗，国家国旗，呈长方形，长宽之比约为1.618：1。
多哥国旗，由三道绿色横条和两道黄色横条相间排列组成，旗面左上角为一红色正方形，其正中有一颗白色五角星。
绿色代表农业，又象征希望；黄色象征国家的矿藏，还表示人民的信心和对祖国命运的关心；红色象征人类的真诚、博爱与献身精神；白色象征纯洁；五角星象征国家的独立和人民新生。
"""

import turtle

h = 600
w = h * 1.618
item = h / 5

turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)

#条纹
colors = ["#006a4e","#fece00","#006a4e","#fece00","#006a4e"]
for j in range(0,5):
    t.pencolor(colors[j])
    t.fillcolor(colors[j])
    t.penup()
    t.goto(w/2,h/2 - item * j)
    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.right(90)
        if i % 2 == 0:
            t.fd(item)
        else:
            t.fd(w)
    t.end_fill()

#红
t.penup()
t.goto(-w/2,h/2)
t.pendown()
t.pencolor("#d21033")
t.fillcolor("#d21033")
t.begin_fill()
for i in range(4):
    t.fd(item*3)
    t.right(90)
t.end_fill()

#星
t.pencolor("white")
t.fillcolor("white")
t.penup()
t.home()
t.goto(-item *3.3,item+25)
t.pendown()
t.begin_fill()
for _ in range(5):
   t.forward(item * 1.5)
   t.right(144)
t.end_fill()

t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="多哥鲜国旗.eps") #将图片保存下来

turtle.done()