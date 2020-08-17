import turtle

from random import randrange

turtle.getscreen ()

t = turtle.Turtle()

t.pencolor ("white")

t.speed (10)

def kwadrat (bok):
    t.up ()
    t.goto (randrange ((-400 + bok), (400 - bok)), randrange ((-300 + bok), (300 - bok)))
    t.down()
    t.begin_fill ()
    i = 0
    while i < 4:
        t.fd (bok)
        t.lt (90)
        i+=1
    t.end_fill ()

def test (n, bok, kolor):
    t.fillcolor (kolor)
    a = 0
    while a < n:
        kwadrat (bok)
        a+=1


if __name__ == '__main__':
    test (10, 10, "orange")
