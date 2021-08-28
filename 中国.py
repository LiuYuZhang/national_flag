"""
 中国国旗
 根据1949年9月28日中国人民政治协商会议第一届全体会议主席团公布的《国旗制法说明》，中华人民共和国国旗旗面为红色，长方形，其长与高为三与二之比，旗面左上方缀黄色五角星五颗。
 一星较大，其外接圆直径为旗高十分之三，居左；四星较小，其外接圆直径为旗高十分之一，环拱于大星之右。
"""

import turtle

w,h  = 960,640 #《国旗法》对国旗的制作有明确规范。国旗尺寸分6种规格（单位CM）： 1号，288×192； 2号，240×160； 3号，192×128； 4号，144×96； 5号，96×64； 6号，66×44。
turtle.screensize(w,h,"white")
turtle.setup(width=w, height=h)  # 设置画布大小

t = turtle.Turtle()
t.pensize(1)
t.speed(0)

#红
t.pu()
t.goto(-w/ 2,h / 2)
t.pd()
t.color("#ee1c25")
t.begin_fill()
for i in range(4):
    if i % 2 == 0:
        t.fd(w)
    else:
        t.fd(h)
    t.rt(90)
t.end_fill()

item = w / 2 / 15
#大星
t.color("#ffff00")
t.pu()
t.goto(- item * 13, item * 6)  #定位到大星最左侧点
t.pd()
t.begin_fill()
for i in range(5):
    t.fd(h / 10 * 3) #外接圆直径为旗高十分之三
    t.right(144)
t.end_fill()

#https://www.sohu.com/a/337652121_587438
#小星
t.pu()
t.home()
t.goto(- item * 6, item * 9)
t.seth(305)
t.pd()
t.begin_fill()
for i in range(5):
    t.fd(h / 10)
    t.left(144)
t.end_fill()

t.pu()
t.goto(- item * 6, item * 1)
t.seth(30)
t.pd()
t.begin_fill()
for i in range(5):
    t.fd(h / 10)
    t.left(144)
t.end_fill()

t.pu()
t.seth(5)
t.goto(- item * 4, item * 6)
t.pd()
t.begin_fill()
for i in range(5):
    t.fd(h / 10)
    t.left(144)
t.end_fill()

t.pu()
t.home()
t.goto(- item * 4, item * 4)
t.seth(-10)
t.pd()
t.begin_fill()
for i in range(5):
    t.fd(h / 10)
    t.right(144)
t.end_fill()

# t.hideturtle()


#todo放弃
ts = t.getscreen()
ts.getcanvas().postscript(file="中国国旗.eps") #将图片保存下来

turtle.mainloop()
