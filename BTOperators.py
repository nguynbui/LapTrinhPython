import math


def ex01():
    b = float(input("Base = "))
    h = float(input("Height = "))
    print(f'Area = {0.5*b*h}')

def ex02():
    a = float(input('Enter side a: '))
    b = float(input('Enter side b: '))
    c = float(input('Enter side c: '))

    print(f'Perimeter of the triangle = {a + b + c}')

def ex03():
    length = float(input('Length = '))
    width = float(input('Width = '))

    print(f'Area = {length * width}')
    print('\n')
    print(f'Perimeter = {2 * (length + width)}')

def ex04():
    pi = 3.14
    rad = float(input('Radius = '))

    print(f'Area = {pi * rad * rad}')
    print('\n')
    print(f'Circumference = {2 * pi * rad}')

def ex06():
    (x1, y1) = (2, 2)
    (x2, y2) = (6, 10)
    m = (y2 - y1)/(x2 - x1)

    print(f'm = {m}')
    print(f'Euclidean distance = {math.sqrt((x2 - x1)**2 + (y2 - y1)**2)}')

if __name__ == '__main__':
    ex06()