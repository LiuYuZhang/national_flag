

"""
日本国国旗是日本国的国旗，又名日章旗、太阳旗，呈长方形，长宽比例为3:2，圆形上下的空隙相同，圆形的直径为旗帜长度的五分之三，圆形的中心点与旗面的中心点重合
"""
import turtle
width = 900 #国旗宽度
height = 600 #国旗高度
turtle.screensize(width,height,"white") #设置画布宽高及颜色
turtle.setup(width=width,height=height)

r = int(height / 5 *3 /2) #国旗半径
t = turtle.Turtle()
#移动画笔
t.penup()
t.goto(0,-r)
t.pendown()

#设置画笔属性
t.pensize(1)
t.pencolor("#ff0000") #画笔颜色
t.fillcolor("#ff0000") #画笔填充颜色
t.hideturtle() #隐藏乌龟
t.speed(10) #控制画笔速度

t.begin_fill()
t.circle(r)
t.end_fill()

turtle.mainloop()