"""
苏里南国旗
苏里南共和国国旗采用于1975年11月25日，呈长方形，长与宽之比为3：2。旗面自上而下由绿、白、红、白、绿五个平行长条组成，红、绿、白条的宽度之比为4：2：1。
旗面中央有一颗黄色五角星，象征民族的团结和光明的前途；绿色代表丰富的自然资源和肥沃的土地，也象征人民对新苏里南的期望；白色象征正义和自由；红色象征热情和进步，也表示为祖国献出全部力量的愿望。
"""

import turtle

width = 900
height = 602
turtle.screensize(width,height,"white")
turtle.setup(width=width,height=height)
item = height / 10 

t = turtle.Turtle()
t.pensize(1)
t.speed(10)


#绿
t.penup()
t.goto(0,height/2 -  2 *item)
t.pendown()
t.pencolor("#00722a")
t.fillcolor("#00722a")
t.forward(width/2)
t.left(90)
t.begin_fill()
t.forward(item * 2)
t.left(90)
t.forward(width)
t.left(90)
t.forward(item * 2)
t.left(90)
t.forward(width / 2)
t.end_fill()

#白
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
t.begin_fill()
t.forward(width/2)
t.right(90)
t.fd(item)
t.right(90)
t.fd(width)
t.right(90)
t.fd(item)
t.right(90)
t.fd(width)
t.end_fill()

#红色
t.right(90)
t.fd(item)
t.pencolor("#d21033")
t.fillcolor("#d21033")
t.begin_fill()
t.fd(4 * item)
t.right(90)
t.fd(width)
t.right(90)
t.fd(4 * item)
t.right(90)
t.fd(width)
t.end_fill()


#白
t.pencolor("white")
t.fillcolor("white")
t.penup()
t.goto(width/ 2,-item *2)
t.pendown()
t.begin_fill()
t.right(90)
t.fd(item)
t.right(90)
t.fd(width)
t.right(90)
t.fd(item)
t.right(90)
t.fd(width)
t.end_fill()

#绿
t.right(90)
t.fd(item)
t.pencolor("#00722a")
t.fillcolor("#00722a")
t.begin_fill()
t.fd(item * 2)
t.right(90)
t.fd(width)
t.right(90)
t.fd(item * 2)
t.right(90)
t.fd(width)
t.end_fill()
t.hideturtle()

#星
t.penup()
t.goto(- 120,30)
t.pendown()

t.pencolor("#fece00")
t.fillcolor("#fece00")
t.begin_fill()
for _ in range(5):
   t.forward(item * 4)
   t.right(144)
t.end_fill()


ts = t.getscreen()
ts.getcanvas().postscript(file="苏里南国旗.eps") #将图片保存下来

turtle.done()
