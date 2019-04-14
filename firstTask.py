from tkinter import *
import math


# вычисление значения функции
def func(x):
    # return math.sin(x)
    return x*x
    # return x
    # return x*math.sin(x*x)


# нахождение максимального и минимального значения функции
def max_min():
    ymin = ymax = func(a)
    for xx in range(500):
        x = a + xx*(b - a)/500
        y = func(x)
        if y < ymin:
            ymin = y
        if y > ymax:
            ymax = y
    return ymin, ymax


# вычисление у по х, масштабирование, поиск координаты у для отрисовки оси ОХ
def calculate(xx, x_0, old_y):
    x = a + xx*(b - a)/500
    y = func(x)
    yy = (y - ymax)*500/(ymin - ymax)
    if y == 0:
        x_0 = yy
    elif (y > 0) and (old_y < 0):
        if y < 0 - old_y:
            x_0 = yy
        else:
            x_0 = (old_y - ymax)*500/(ymin - ymax)
    old_y = y
    return yy, x_0, old_y


# отрисовка осей
def drow_axis(x):
    if x is not None:
        canvas.create_line(0, x, 500, x, fill="black", arrow=LAST)
            # elif round(ymin, 2) == 0:
            #     canvas.create_line(0, x, 500, x, fill="black", arrow=LAST)


# поиск координаты х для отрисовки оси ОУ, отрисовка
def find_ordinate_coord():
    drawn_axis_OY = False
    if a == 0:
        canvas.create_line(0, 500, 0, 0, fill="black", arrow=LAST)
        drawn_axis_OY = True
    else:
        for xx in range(500):
            x = a + xx * (b - a) / 500
            if (x == 0) and (drawn_axis_OY is False):
                canvas.create_line(xx, 500, xx, 0, fill="black", arrow=LAST)
                drawn_axis_OY = True
            if x > 0:
                x_old = a + (xx - 1) * (b - a) / 500
                if (0 - x_old < x) and (drawn_axis_OY is False):
                    canvas.create_line(xx - 1, 500, xx - 1, 0, fill="black", arrow=LAST)
                    drawn_axis_OY = True
                elif drawn_axis_OY is False:
                    canvas.create_line(xx, 500, xx, 0, fill="black", arrow=LAST)
                    drawn_axis_OY = True


def main():
    global ymin
    global ymax
    drawn_abscissa = False;
    ymin, ymax = max_min()
    yy = (func(a) - ymin)*500/(ymax - ymin)
    yy_old = yy
    y_old = ymin
    abscissa_coord = yy
    for xx in range(0, 500):
        yy, abscissa_coord, old = calculate(xx, abscissa_coord, y_old)
        canvas.create_line(xx, yy_old, xx + 1, yy, fill="#ff0000")
        yy_old = yy
        y_old = old
    ordinate_coord = find_ordinate_coord()
    # drow_axis(abscissa_coord)


if __name__ == "__main__":
    global a
    global b
    print("введите 2 числа:")
    a = int(input())
    b = int(input())
    root = Tk()
    canvas = Canvas(root, width=500, height=500, bg='white')
    canvas.pack()
    main()
    root.mainloop()



