"""
帕劳共和国国旗
帕劳共和国（The Republic of Palau），简称帕劳（中国台湾将其译名为：帛琉），位于西太平洋，是太平洋进入东南亚的门户之一，首都梅莱凯奥克。
帕劳国旗呈长方形，长与宽之比为8:5。旗地为蓝色，象征海洋。中间偏左处有一轮金色圆月，象征民族团结和结束外国统治。
本国旗启用于1981年1月1日。帕劳独立前曾使用过联合国旗、美国国旗和太平洋岛屿托管地旗。金黄色的圆轮代表月亮，月亮在帕劳人心目中是安定、和平与爱的象征。
蓝色代表浩涵的太平洋，又象征自由、独立和主权。
"""

import turtle
width = 800 #国旗宽度
height = 500 #国旗高度
turtle.screensize(width,height,"#4aadd6") #设置画布宽高及颜色
turtle.setup(width=width,height=height)

r = int(height / 5 *3 /2) #国旗半径
t = turtle.Turtle()
#移动画笔
t.penup()
t.goto(-100,-r)
t.pendown()

#设置画笔属性
t.pensize(1)
t.pencolor("#ffde00") #画笔颜色
t.fillcolor("#ffde00") #画笔填充颜色
t.hideturtle() #隐藏乌龟
t.speed(10) #控制画笔速度

t.begin_fill()
t.circle(r)
t.end_fill()

turtle.mainloop()

