import turtle

t = turtle

my_win = t.Screen()

my_win.bgcolor("light blue")
my_win.title("leg")

size = 0

while True:
    for i in range(4):
        t.forward(size+1)
        t.left(90)
        size = size - 5
    size = size + 1


t.done

