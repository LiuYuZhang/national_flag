"""
科特迪瓦国旗
科特迪瓦全称科特迪瓦共和国，科特迪瓦在法语的意思是“象牙海岸”，应该国政府要求，中华人民共和国用音译名为科特迪瓦，首都是亚穆苏克罗。
科特迪瓦国旗采用于1959年，并于1960年8月7日独立时启用。国旗呈长方形，长与宽之比为3：2。旗面由三个平行相等的竖长方形构成，从左至右依次为橙、白、绿三色。
橙色代表北部的热带大草原，也象征国家的繁荣富强与人民的爱国精神；白色象征南、北方的和平团结的希望；绿色代表南部地区的原始森林中丰富的自然资源。
橙、白、绿三色还分别解释为：民族爱国精神、和平与纯洁、对未来的希望
"""

import turtle
from typing import ItemsView

w = 900
h = 600
item = w / 3

turtle.screensize(w,h,"white")
turtle.setup(w,h)

#橙
t = turtle.Turtle()
t.pensize(1)
t.speed(10)

t.pencolor("#f77f00")
t.fillcolor("#f77f00")
t.penup()
t.goto(-item/2,0)
t.pendown()
t.begin_fill()
t.left(90)
t.forward(h//2)
t.left(90)
t.fd(item)
t.left(90)
t.fd(h)
t.left(90)
t.fd(item)
t.end_fill()

#白
t.pencolor("#ffffff")
t.fillcolor("#ffffff")
t.begin_fill()
t.forward(item)
t.left(90)
t.fd(h)
t.left(90)
t.fd(item)
t.left(90)
t.end_fill()
t.right(270)
t.forward(item)

#绿
t.pencolor("#009e60")
t.fillcolor("#009e60")
t.begin_fill()
t.fd(item)
t.right(90)
t.fd(h)
t.right(90)
t.fd(item)
t.end_fill()

t.hideturtle()



turtle.done()

