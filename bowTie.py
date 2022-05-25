import turtle as t


def goto(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def init():
    t.setup(800, 800)
    t.pensize(10)
    t.pencolor("red")
    t.speed(14)


def jiexin():
    m, n = 0, 200
    for i in range(11):
        goto(m, n)
        t.seth(-45)
        t.fd(200)
        m -= 20/pow(2, 0.5)
        n -= 20/pow(2, 0.5)

    m, n = 0, 200
    for j in range(11):
        goto(m, n)
        t.seth(-135)
        t.fd(200)
        m += 20/pow(2, 0.5)
        n -= 20/pow(2, 0.5)


def jiexiaoban():
    m = -20/pow(2, 0.5)
    n = 200-20/pow(2, 0.5)
    for k in range(4):
        goto(m, n)
        t.seth(135)
        t.fd(20)
        t.circle(10, 180)
        t.fd(20)
        m -= 40/pow(2, 0.5)
        n -= 40/pow(2, 0.5)

    m = 20/pow(2, 0.5)
    n = 200-20/pow(2, 0.5)
    for k in range(4):
        goto(m, n)
        t.seth(45)
        t.fd(20)
        t.circle(-10, 180)
        t.fd(20)
        m += 40/pow(2, 0.5)
        n -= 40/pow(2, 0.5)

    m = 20/pow(2, 0.5)
    n = 200-200*pow(2, 0.5)+20/pow(2, 0.5)
    for k in range(4):
        goto(m, n)
        t.seth(-45)
        t.fd(20)
        t.circle(10, 180)
        t.fd(20)
        m += 40/pow(2, 0.5)
        n += 40/pow(2, 0.5)

    m = -20/pow(2, 0.5)
    n = 200-200*pow(2, 0.5)+20/pow(2, 0.5)
    for k in range(4):
        goto(m, n)
        t.seth(-135)
        t.fd(20)
        t.circle(-10, 180)
        t.fd(20)
        m -= 40/pow(2, 0.5)
        n += 40/pow(2, 0.5)


def waiyuan():
    goto(90*pow(2, 0.5), 200-110*pow(2, 0.5))
    t.seth(-45)
    t.circle(20, 270)

    goto(-90*pow(2, 0.5), 200-110*pow(2, 0.5))
    t.seth(-135)
    t.circle(-20, 270)

    goto(80*pow(2, 0.5), 200-120*pow(2, 0.5))
    t.seth(-45)
    t.circle(40, 270)

    goto(-80*pow(2, 0.5), 200-120*pow(2, 0.5))
    t.seth(-135)
    t.circle(-40, 270)


def shengzi():
    goto(0, 200)
    t.pensize(20)
    t.seth(90)
    t.fd(60)
    goto(0, 320)
    t.pensize(12)
    t.seth(180)
    t.circle(30, 360)

    goto(0, 200-200*pow(2, 0.5))
    t.pensize(40)
    t.seth(-90)
    t.fd(20)
    t.pensize(2)
    s = -20
    for i in range(11):
        goto(s, 200-200*pow(2, 0.5))
        t.seth(-90)
        t.fd(200)
        s += 4


def hanzi():
    goto(-200, 330)
    t.write("Happy Chinese Knot", font=("Arial", 40, "normal"))


def main():
    init()
    jiexin()
    jiexiaoban()
    waiyuan()
    shengzi()
    hanzi()
    t.hideturtle()
    t.done()


main()
