"""
芬兰国旗    
芬兰共和国（芬兰语：Suomen tasavalta，瑞典语：Republiken Finland），简称芬兰（芬兰语：Suomi，瑞典语：Finland），位于欧洲北部，北欧五国之一。
芬兰国旗名为“蓝色十字”旗（芬兰语：Siniristilippu），1818年5月正式定为国家市民旗帜。”呈长方形，长与宽之比为18∶11。旗地为白色。
稍偏左侧的十字形蓝色宽条将旗面分为四个白色长方形。芬兰以“千湖之国”著称，西南临波罗的海，旗上的蓝色象征湖泊，河流和海洋；另一说象征蓝天。
蓝色和白色国旗也象征着与芬兰19世纪曾经是沙皇俄国的大公国。
"""

import turtle

w = 900
h = 550
item = 164

turtle.screensize(w,h,"white")
turtle.setup(w,h)
t = turtle.Turtle()
t.speed(10)
t.pensize(1)
t.hideturtle()


#底色框
t.pencolor("white")
t.fillcolor("white")
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

#横向蓝块
t.penup()
t.pencolor("#003580")
t.fillcolor("#003580")
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


#纵向蓝块
t.penup()
t.goto(-item/2+30,h/2)
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
ts.getcanvas().postscript(file="芬兰国旗.eps") #将图片保存下来

turtle.done()