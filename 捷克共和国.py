"""
捷克共和国国旗
捷克共和国，简称“捷克”，与德国，奥地利，波兰，斯洛伐克四国接壤，是位于中欧的一个内陆国家，首都为布拉格。捷克国旗呈长方形，长宽之比为3:2。
旗面由蓝、白、红三色组成。左侧为蓝色等腰三角形。右侧是两个相等的梯形，上白下红。蓝、白、红三色是斯拉夫民族喜欢的传统颜色。
捷克人的故乡是古老的波希米亚王国，这个王国的颜色为红、白两色。白色代表神圣和纯洁，象征着人民对和平与光明的追求；
红色象征勇敢和不畏困难的精神，象征人民为国家的独立解放和繁荣富强而奉献的鲜血与取得的胜利。
蓝色来自原来的摩拉维亚和斯洛伐克省徽章的颜色。
"""

import turtle
import math

w = 900
h = 600
item = h / 2
c = math.sqrt((math.pow(item,2) + math.pow(w/2,2))) #三角形边长
print(c)
turtle.screensize(w,h,"white")
turtle.setup(w,h)


t = turtle.Turtle()
t.pensize(1)
t.speed(10)
# t.hideturtle()

#白
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
t.begin_fill()
t.forward(w/2)
t.left(90)
t.forward(item)
t.left(90)
t.forward(w)
t.left(90)
t.forward(item)
t.left(90)
t.forward(w/2)
t.end_fill()


#红
t.pencolor("#d7141a")
t.fillcolor("#d7141a")
t.begin_fill()
t.forward(w/2)
t.right(90)
t.forward(item)
t.right(90)
t.forward(w)
t.right(90)
t.forward(item)
t.right(90)
t.forward(w/2)
t.end_fill()


#三角
t.pencolor("#11457e")
t.fillcolor("#11457e")

t.begin_fill()
t.left(146.6)
t.forward(c)
t.left(123.4)
t.forward(h)
t.end_fill()

t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="捷克共和国国旗.eps") #将图片保存下来

turtle.done()