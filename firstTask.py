from tkinter import *
import math


def func(x):
    # return x*math.sin(x*x)
    return x*x
    # return x


def max_min(a, b):
    y_0 = None
    ymin = ymax = func(a)
    for xx in range(500):
        x = a + xx*(b - a)/500
        if x == 0:
            y_0 = xx
        y = func(x)
        if y < ymin:
            ymin = y
        if y > ymax:
            ymax = y
    return ymin, ymax, y_0


def calculate(xx, a, b, miny, maxy, x_0):
    x = a + xx*(b - a)/500
    y = func(x)
    yy = (y - maxy)*500/(miny - maxy)
    if y == 0:
        x_0 = yy
    return yy, x_0


def drow_axis(x, y):
    if x is not None:
        canvas.create_line(0, x, 500, x, fill="black", arrow=LAST)
    if y is not None:
        canvas.create_line(y, 500, y, 0, fill="black", arrow=LAST)


def main(a, b):
    x_axis_coord = None
    miny, maxy, y_axis_coord = max_min(a, b)
    yy = (func(a) - miny)*500/(maxy - miny)
    yy_old = yy
    for xx in range(0, 500):
        yy, x_axis_coord = calculate(xx, a, b, miny, maxy, x_axis_coord)
        canvas.create_line(xx, yy_old, xx + 1, yy, fill="#ff0000")
        yy_old = yy
    drow_axis(x_axis_coord, y_axis_coord)


if __name__ == "__main__":
    print("введите 2 числа:")
    a = int(input())
    b = int(input())
    root = Tk()
    canvas = Canvas(root, width=500, height=500, bg='white')
    canvas.pack()
    main(a, b)
    root.mainloop()



