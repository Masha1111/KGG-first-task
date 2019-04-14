from tkinter import *
import math


# вычисление значения функции
def func(x):
    # return math.sin(x)
    # return x*x
    # return x
    return x*math.sin(x*x)


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


# вычисление у по х, масштабирование
def calculate(xx, old_y, flag):
    x = a + xx*(b - a)/500
    y = func(x)
    yy = (y - ymax)*500/(ymin - ymax)
    if y < 0:
        flag[1] = True
    if y > 0:
        flag[2] = True
    if y == 0:
        flag[0] = True
        flag[3] = yy
    old_y = y
    return yy, old_y, flag


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


# поиск координаты y для отрисовки оси ОX, отрисовка
def find_abscissa_coord(flag, y_min, y_max):
    if flag[0] is True:
        canvas.create_line(0, flag[3], 500, flag[3], fill="black", arrow=LAST)
    else:
        if (flag[1] is True) and (flag[2] is True):
            old_y = y_min
            diff = y_max - y_min
            for xx in range(500):
                x = a + xx * (b - a) / 500
                y = func(x)
                yy = (y - ymax) * 500 / (ymin - ymax)
                if (((old_y < 0) and (y > 0)) or ((old_y > 0) and (y < 0))) and (math.fabs(y - old_y) < diff):
                    yy_old = (old_y - ymax) * 500 / (ymin - ymax)
                    diff = math.fabs(old_y - y)
                    if math.fabs(old_y) < math.fabs(y):
                        coord = yy_old
                    else:
                        coord = yy
                old_y = y
            canvas.create_line(0, coord, 500, coord, fill="black", arrow=LAST)



def main():
    global ymin
    global ymax
    ymin, ymax = max_min()
    yy = (func(a) - ymin)*500/(ymax - ymin)
    yy_old = yy
    y_old = ymin
    y_0_flag = [False, None, None, None]
    for xx in range(0, 500):
        yy, old, flag = calculate(xx, y_old, y_0_flag)
        canvas.create_line(xx, yy_old, xx + 1, yy, fill="#ff0000")
        yy_old = yy
        y_old = old
        y_0_flag = flag
    find_ordinate_coord()
    find_abscissa_coord(y_0_flag, ymin, ymax)


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



