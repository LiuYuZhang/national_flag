"""
博茨瓦纳国旗
博茨瓦纳（Botswana）又译为波札那，全称博茨瓦纳共和国，是位于非洲南部的内陆国，首都哈博罗内。博茨瓦纳国旗呈长方形，长宽之比为3∶2。
旗面中间横贯一道黑色宽条，上下为两个淡蓝色的横长方形，黑色与淡蓝色之间是两道白色细条。黑色代表博茨瓦纳人口中的绝大部分黑人；白色代表白人等人口中的少数部分；蓝色象征蓝天和水。
国旗的寓意是在非洲的蓝天下，黑人和白人团结、生活在一起。
"""

import turtle

width = 900
height = 600
turtle.screensize(width,height,"white")
turtle.setup(width=width,height=height)

white_h = height * 0.26

t = turtle.Turtle()
t.pensize(1)
t.speed(10)


#画蓝
t.pencolor("#76aada")
t.fillcolor("#76aada")
t.forward(width/2)
t.left(90)
t.begin_fill()
t.forward(height/2)
t.left(90)
t.forward(width)
t.left(90)
t.forward(height)
t.left(90)
t.forward(width)
t.left(90)
t.forward(height/2)
t.end_fill()

#白色
t.pencolor("white")
t.fillcolor("white")
t.begin_fill()
t.forward(white_h/2)
t.left(90)
t.forward(width)
t.left(90)
t.forward(white_h)
t.left(90)
t.forward(width)
t.left(90)
t.forward(white_h)
t.end_fill()

#黑色
t.left(180)
t.forward(white_h * 0.16)
t.pencolor("#000000")
t.fillcolor("#000000")
t.begin_fill()
t.right(90)
t.forward(width)
t.left(90)
t.forward(white_h*0.68)
t.left(90)
t.forward(width)
t.left(90)
t.forward(white_h*0.68)
t.end_fill()

t.hideturtle()


ts = t.getscreen()
ts.getcanvas().postscript(file="博茨瓦纳国旗.eps") #将图片保存下来

turtle.done()
