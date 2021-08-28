"""
 玻利维亚国旗
 多民族玻利维亚国（Plurinational State of Bolivia），简称玻利维亚，是位于南美洲中部的内陆国家，周边与巴西、秘鲁、智利、阿根廷、巴拉圭五国相邻，法定首都为苏克雷，
 实际政府驻地为拉巴斯。玻利维亚国旗启用于1851年10月31日，国旗呈长方形，长宽之比为3：2。
 旗面自上而下由红黄绿三个平行相等的长方形组成，中间绘有国徽。原来红色象征为国献身，黄色象征希望，绿色象征神圣国土。
 现则分别代表玻的动物，矿产和植物。正式场合用带国徽的国旗，一般场合用不带国徽的国旗
"""

import turtle

w = 900
h = 450
turtle.screensize(w,h,"white")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
t.speed(10)
t.hideturtle()

#顶部红色
t.pencolor("#ff1b06")
t.fillcolor("#ff1b06")
t.begin_fill()
t.penup()
t.goto(0,h/3/2)
t.pendown()
t.pendown()
t.forward(w/2)
t.left(90)
t.forward(h/3)
t.left(90)
t.forward(w)
t.left(90)
t.forward(h/3)
t.left(90)
t.forward(w/2)
t.end_fill()


#中间蓝色
t.pencolor("#ffef00")
t.fillcolor("#ffef00")
t.begin_fill()
t.penup()
t.goto(0,-h/3/2)
t.pendown()
t.pendown()
t.forward(w/2)
t.left(90)
t.forward(h/3)
t.left(90)
t.forward(w)
t.left(90)
t.forward(h/3)
t.left(90)
t.forward(w/2)
t.end_fill()

#底部橙色
t.pencolor("#009d00")
t.fillcolor("#009d00")
t.begin_fill()
t.penup()
t.goto(0,-h/3-h/3/2)
t.pendown()
t.pendown()
t.forward(w/2)
t.left(90)
t.forward(h/3)
t.left(90)
t.forward(w)
t.left(90)
t.forward(h/3)
t.left(90)
t.forward(w/2)
t.end_fill()

turtle.mainloop()
