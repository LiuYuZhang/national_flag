"""
老挝国旗
老挝人民民主共和国，简称老挝。是一个位于中南半岛北部的内陆国家，北邻中国，南接柬埔寨，东临越南，西北毗邻缅甸，西南毗邻泰国，首都万象。
老挝的国歌为《老挝人民颂歌》，老挝国旗是以红色、蓝色及白色为主色，国旗旗面中间的平行长方形为蓝色，占旗地一半，上下为红色的长方形，各占旗地四分之一。
蓝色展开一片富饶美丽的国土，表示人民热爱和平安宁的生活。红色象征革命，表明不惜以鲜血为代价捍卫国家尊严。蓝色部分中间为白色圆轮，轮的直径为蓝色部分宽度的五分之四。长宽比为3:2。
白色圆形象征老挝人民在党的领导下团结一致以及国家光明的未来。白色圆形也代表满月，置于蓝条之上，象征皎洁明月高悬于湄公河的上空。此旗原为老挝爱国战线旗帜。
"""

import turtle
from typing import ItemsView

width = 900
height = 600
turtle.screensize(width,height,"white")
turtle.setup(width=width,height=height)
item = height / 4

t = turtle.Turtle()
t.pensize(1)
t.speed(10)


#红色
t.penup()
t.goto(0,height/2)
t.pendown()
t.pencolor("#ce1126")
t.fillcolor("#ce1126")
t.left(90)
t.begin_fill()
t.right(90)
t.forward(width/2)
t.right(90)
t.forward(item)
t.right(90)
t.forward(width)
t.right(90)
t.forward(item)
t.right(90)
t.forward(width/2)
t.end_fill()

#蓝色
t.penup()
t.goto(0,height/2 - item)
t.pendown()
t.pencolor("#002868")
t.fillcolor("#002868")
t.begin_fill()
t.forward(width/2)
t.right(90)
t.forward(item * 2)
t.right(90)
t.forward(width)
t.right(90)
t.forward(item * 2)
t.right(90)
t.end_fill()


#红色
t.penup()
t.goto(0,-height/2)
t.pendown()

t.pencolor("#ce1126")
t.fillcolor("#ce1126")
t.begin_fill()
t.fd(width / 2)
t.left(90)
t.fd(item)
t.left(90)
t.fd(width)
t.left(90)
t.fd(item)
t.left(90)
t.fd(width / 2)
t.end_fill()


#明月
t.pencolor("white")
t.fillcolor("white")
t.penup()
t.goto(0,-item*0.8)
t.pendown()

t.begin_fill()
t.circle(item*0.8)
t.end_fill()

t.hideturtle()

ts = t.getscreen()
ts.getcanvas().postscript(file="老挝国旗.eps") #将图片保存下来

turtle.done()
