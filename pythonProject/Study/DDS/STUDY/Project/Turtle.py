from turtle import *

title("Test")
speed(0)
x = 1
bgcolor("black")
pencolor("white")
while x < 5000:
    forward(5 + x)
    right(91)
    x += 1
mainloop()
