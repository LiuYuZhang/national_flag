"""
乌克兰国旗
乌克兰（Ukraine），位于欧洲东部，东接俄罗斯、南濒黑海，北与白俄罗斯毗邻、西与波兰、斯洛伐克、匈牙利、罗马尼亚和摩尔多瓦诸国相连，首都为基辅。
乌克兰国旗呈长方形，由上蓝下黄两块平行相等的横长方形组成，长与宽之比为3∶2。
乌克兰曾于1917年建立乌克兰苏维埃社会主义共和国，1922年成为原苏联的一个加盟共和国，1952年起采用和原苏联国旗相似的带五角星及镰刀、铁锤图案的红旗，只是旗面下部为蓝色宽边。
1991年宣布独立，1992年恢复乌克兰人民共和国的蓝、黄两色旗为国旗。
"""

import turtle

w = 900
h = 600
turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)
t.hideturtle()

#顶部蓝色
t.pencolor("#005bbb")
t.fillcolor("#005bbb")
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


#底部黄色
t.pencolor("#ffd500")
t.fillcolor("#ffd500")
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
ts.getcanvas().postscript(file="乌克兰国旗.eps") #将图片保存下来

turtle.done()