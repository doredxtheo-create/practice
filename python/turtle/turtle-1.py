import turtle
t = turtle

t.Screen().bgcolor("orange")
t.Screen().setup(300,400)

num_sides = 6

side_len = 70

angle = ( 360.0 / num_sides )

for i in range(num_sides):
    t.forward(side_len)
    t.right(angle)

t.done()

