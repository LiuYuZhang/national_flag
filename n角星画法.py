

import turtle
import math

n = 7 #边个数
l = 50 #边长

i=0#循环变量
if n%2==1:#奇数ｎ角星的画法
    while i < n:
        turtle.forward(l)
        turtle.left(180 - (180 / n))
        i+=1
    turtle.done()
else :#偶数ｎ角形画法
    n1 = n / 2 # n的一半
    a = (180 * (n - 2) / n) # 正n边形内角
    b = 180 - a # n角形的内角
    c = b / 2 # 长方形短边与ｌ围城三角形的短边的对角
    d = 180 - (c * (n / 2 - 1))#ｌ的对角
    d1 = (d / 180) * math.pi#转化为三角函数
    c1 = (c / 180) * math.pi
    e = (math.sin(c1) / math.sin(d1)) * l#长方形的短边
    
#奇数n角星可以一笔画出，偶数n角星看为n/2个长方形长边组成。

while i < n1:
    turtle.forward(l)
    turtle.left(90)
    turtle.penup()
    turtle.forward(e)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(l)
    turtle.left(180 - 180 / n1)
    i+=1
turtle.done()