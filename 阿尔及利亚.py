"""
阿尔及利亚，全称阿尔及利亚民主人民共和国，是非洲北部马格里布的一个国家，首都是阿尔及尔。阿尔及利亚民主人民共和国国旗呈长方形，长与宽之比为3∶2。
旗面由左绿右白两个平行相等的竖长方形组成，中央为一弯红色新月和一颗稍微倾斜的红色五角星。
绿色象征未来的希望，白色代表纯洁与和平，红色象征革命和为理想而奋斗的献身精神。阿尔及利亚以伊斯兰教为国教，新月和五角星是这个穆斯林国家的象征。
"""

import turtle

width = 900
height = 600
turtle.screensize(width,height,"white")
turtle.setup()

t = turtle.Turtle()

#左侧绿色
t.pencolor("#006233")
t.fillcolor("#006233")
t.speed(10)
t.penup()
t.goto(-(width  / 2),-(height / 2))
t.pendown()
t.begin_fill()
t.forward(width / 2)
t.left(90)
t.forward(height)
t.left(90)
t.forward(width/2)
t.end_fill()

#红色新月 d21034


turtle.mainloop()