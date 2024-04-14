import turtle
s = turtle.Screen()
t = turtle.Turtle()
# t.speed(5)
# t.right(90)
# t.color("red")
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)
# t.right(90)
# t.forward(100)

# t.clear()

# for i in range(4):
#     t.right(90)
#     t.forward(100)

s.title("figuros")
t.pencolor("green")
for i in range(3, 13):
    for j in range(i):
        t.left(360/i**2)
        t.forward(3)






s.exitonclick()