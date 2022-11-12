
from turtle import *
from math import sqrt
width, height = 800, 600
screen = Screen()     # 创建窗口对象
screen.setup(width, height)    # 设置窗口的宽高
screen.delay(0)    # 设置无延时绘画
screen.bgcolor('pink')     # 设置背景颜色为粉色

# 设置画笔的统一属性
t = Turtle(visible=False, shape='circle')
t.shapesize(10, 10)
t.pencolor('red')
t.fillcolor('red')
t.penup()
# 克隆一个圆形，设置位置
circle1 = t.clone()
circle1.goto(-sqrt(10*10*160)/2, 0)
# 克隆第二个圆形，设置位置
circle2 = t.clone()
circle2.goto(sqrt(10*10*160)/2, 0)
# 克隆一个正方形，设置位置并旋转角度
square = t.clone()
square.shape("square")
square.setheading(45)
square.goto(0, -sqrt(10*10*160)/2)
# 显示图形
circle1.showturtle()
circle2.showturtle()
square.showturtle()
done()

