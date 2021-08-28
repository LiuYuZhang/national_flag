''''
孟加拉人民共和国（People's Republic of Bangladesh，Bangladesh），简称“孟加拉国”，南亚国家，位于孟加拉湾之北，首都是达卡，国歌为《金色的孟加拉》，孟加拉国国旗呈长方形，
长与宽之比为5：3。旗地为深绿色，中央为红色圆轮。深绿色象征朝气蓬勃、充满生机的祖国绿色大地，象征青春活力和繁荣昌盛；红色圆轮象征经过流血斗争的黑夜之后的黎明。
整个旗面如广阔的平原上正冉冉升起一轮红日，寓意孟加拉人民共和国的光明前景和无限生机
'''
import turtle
width = 900 #国旗宽度
height = 600 #国旗高度
turtle.screensize(width,height,"#006a4e") #设置画布宽高及颜色
turtle.setup(width=width,height=height)

r = int(height / 5 *3 /2) #国旗半径
t = turtle.Turtle()
#移动画笔
t.penup()
t.goto(-100,-r)
t.pendown()

#设置画笔属性
t.pensize(1)
t.pencolor("#f42a41") #画笔颜色
t.fillcolor("#f42a41") #画笔填充颜色
t.hideturtle() #隐藏乌龟
t.speed(10) #控制画笔速度

t.begin_fill()
t.circle(r)
t.end_fill()

turtle.mainloop()