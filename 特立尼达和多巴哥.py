"""
特立尼达和多巴哥国旗
特立尼达和多巴哥（Trinidad and Tobago)国旗采用于1962年，呈长方形，长宽之比为5：3。
红色旗面，一道从左上角斜贯至右下角的黑色宽带将红色旗面分成两个相等的直角三角形，黑色宽带两侧有两道细白边。
红色代表国家和人民的生命力，也象征温暖和太阳的热能；黑色象征人民的力量和献身精神，也象征国家的统一和财富；白色象征国家的未来和海洋。两个三角形代表特立尼达岛和多巴哥岛。
"""

import turtle
import math

w,h = 900,540 #宽、高
item = w / 20


turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)

#红
c = math.sqrt(math.pow(h ,2)+ math.pow(item * 14,2)) #边长
t.pencolor("#ce1127")
t.fillcolor("#ce1127")
t.penup()
t.goto(-w / 2,h/2)
t.pendown()
t.begin_fill()
for i in range(4):
    if i % 2 == 0:
        t.fd(w)
    else:
        t.fd(h)
    t.right(90)
t.end_fill()

#白
t.pencolor("white")
t.fillcolor("white")
t.penup()
t.goto(-w / 2,h/2)
t.pendown()
t.begin_fill()
t.fd(item * 6) 
t.right(40.54)
t.fd(c)
# t.right(139.5)
# t.fd(item * 6)
# t.right(40.5)
# t.fd(c)
t.end_fill()


# t.hideturtle()

#todo 暂缓，使用matplotlib来画

ts = t.getscreen()
ts.getcanvas().postscript(file="特立尼达和多巴哥国旗.eps") #将图片保存下来

turtle.done()