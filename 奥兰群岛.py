"""
    奥兰群岛旗帜是芬兰西海岸讲瑞典语的少数民族聚居的奥兰群岛的区旗，图案是在瑞典国旗的底色中，加上一个象征芬兰的红色十字。
    芬兰的国旗虽然是白色底蓝色十字，但红色和黄色是芬兰国徽的颜色
"""

import turtle

width = 900
height = 600

turtle.screensize(width,height,"#0053a5")
turtle.setup(width,height)
t = turtle.Turtle()
t.speed(10)

t.pencolor("#ffce00")
t.fillcolor("#ffce00")
t.hideturtle()

#横向黄色块
t.penup()
t.goto(0,-170/3)
t.pendown()
t.begin_fill()
t.forward(width / 2)
t.left(90)
t.forward(170)
t.left(90)
t.forward(width)
t.left(90)
t.forward(170)
t.end_fill()

#纵向黄色块
t.penup()
t.goto(0,height/2)
t.pendown()
t.begin_fill()
t.forward(height)
t.right(90)
t.forward(170)
t.right(90)
t.forward(height)
t.end_fill()

#更换画笔颜色
t.pencolor("#d21034")
t.fillcolor("#d21034")

#纵向红色块
t.penup()
t.goto(-170 / 3,height/2)
t.pendown()
t.begin_fill()
t.left(90)
t.forward(170/3)
t.left(90)
t.forward(height)
t.left(90)
t.forward(170/3)
t.end_fill()


#横向红色块
t.penup()
t.goto(-width/2,0)
t.pendown()
t.begin_fill()
t.forward(width)
t.left(90)
t.forward(170/3)
t.left(90)
t.forward(width)
t.left(90)
t.end_fill()

turtle.mainloop()