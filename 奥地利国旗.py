"""
 奥地利国旗
 奥地利共和国（The Republic of Austria），简称“奥地利”（Austria），是一个位于欧洲中部的议会制共和制国家，首都维也纳，是奥地利最大的城市。
 奥地利国旗呈长方形，长与宽之比为3∶2。从上到下由红、白、红三个平行相等的横长方形相连而成，旗面正中是奥地利国徽图案。
 此旗的来历可追溯到奥地利大公国时期，据说当参考资料时的巴本堡公爵在与英王理查一世激战时，公爵的白色军衣几乎全被鲜血染红，只有佩剑处留下一道白痕。
 从此，公爵的军队采用红白红为战旗颜色。1786年约瑟夫二世把红白红旗作为全军战旗，1919年正式定为奥地利国旗。
 奥地利政府机构、部长、总统等官方代表和政府驻外机构均使用带国徽的国旗，一般场合不用带国徽的国旗。
"""

import turtle

w = 900
h = 600
turtle.screensize(w,h,"#ed2939")
turtle.setup(w,h)

t = turtle.Turtle()
t.pensize(1)
#中间白色
t.pencolor("white")
t.fillcolor("white")
t.hideturtle()
t.speed(10)

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

turtle.mainloop()
