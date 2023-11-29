from turtle import Turtle

pipis = Turtle()
pipis.speed(10)


def move_f():
    pipis.forward(1)


def move_b():
    pipis.backward(1)


def rotate_r():
    pipis.right(1)


def rotate_l():
    pipis.left(1)


def home():
    pipis.reset()


pipis.screen.onkeypress(move_f, "w")
pipis.screen.onkeypress(move_b, "s")
pipis.screen.onkeypress(rotate_r, "d")
pipis.screen.onkeypress(rotate_l, "a")
pipis.screen.onkeypress(home, "h")
pipis.screen.listen()
pipis.screen.mainloop()
