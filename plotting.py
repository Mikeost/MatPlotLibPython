import os

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import ConnectionPatch

import numpy as np

from pylab import *

import fileinput

matplotlib.use("TkAgg")

def get_console_data():
    print('Введіть кількість точок:', end = ' ')
    while True:
        try:
            count = int(input())
            break;
        except:
            print('Введіть числове значення!!!')
    
    xList = []
    yList = []

    for i in range(count):
        print('X' + str(i) + ':', end = ' ')
        x = int(input())
        xList.append(x)

        print('Y' + str(i) + ':', end = ' ')
        y = int(input())
        yList.append(y)

    print(xList)
    print(yList)

    plt.plot(xList, yList)
    plt.grid()
    plt.show()

def get_file_data():
    print('Файл повинен мати таку структуру:\n',
          'x0 y0\n',
          'x1 y1\n',
          'xn-1 yn-1\n',
          'Де x & y - координати точок.\n',
          'Наприклад:\n',
          '1 1\n',
          '2 4\n',
          '3 2\n',
          '4 3\n')

    while True:
        try:
            fileName = input('Введіть назву файла: ')
            file = open(fileName, 'r')

            xList = []
            yList = []

            for line in file:
                line = line.split(' ')
                xList.append(int(line[0]))
                yList.append(int(line[1]))

            print(xList)
            print(yList)

            plt.plot(xList, yList)
            plt.grid()
            plt.show()

            return

        except IOError:
            print('Невірна назва файлу')


def simple_graph():
    while True:
        print('\n' + '*' * 50)
        print('\t\t<--Простий графік по точкам-->\n')
        print('Метод занесення данних:')
        print('1. Консоль')
        print('2. Файл')
        print('0. Назад')
        print('\nОберіть номер варіанту:', end = ' ')
        while True:
            try:
                key = int(input())
                break;
            except:
                print('Введіть числове значення!!!')
        print('*' * 50)

        match key:
            case 0:
                break
            case 1:
                get_console_data()
            case 2:
                get_file_data()