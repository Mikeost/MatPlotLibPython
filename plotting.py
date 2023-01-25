import os
import cli

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import ConnectionPatch

import numpy as np

from pylab import *

import fileinput

matplotlib.use("TkAgg")

def get_console_data():
    while True:
        try:
            print('Введіть кількість точок:', end = ' ')
            count = int(input())
            break
        except:
            print('Введіть числове значення!')
    
    if count <= 1:
        return

    xList = []
    yList = []

    for i in range(count):
        while True:
            try:
                print('X' + str(i) + ':', end = ' ')
                x = float(input())
                xList.append(x)
                break
            except:
                print('Введіть числове значення!')

        while True:
            try:
                print('Y' + str(i) + ':', end = ' ')
                y = float(input())
                yList.append(y)
                break
            except:
                print('Введіть числове значення!')

    print(xList)
    print(yList)
    print('*' * 50)

    plt.plot(xList, yList)
    plt.grid()
    plt.show()

def get_file_data():
    print('\nФайл повинен мати таку структуру:\n',
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
                xList.append(float(line[0]))
                yList.append(float(line[1]))

            print(xList)
            print(yList)

            print('*' * 50)

            plt.plot(xList, yList)
            plt.grid()
            plt.show()

            return

        except IOError:
            print('Невірна назва файлу!')


def simple_graph():
    while True:
        cli.clear_screen()
        print('\n' + '*' * 50)
        print('\t\t<--Простий графік по точкам-->\n')
        print('Метод занесення данних:')
        print('1. Консоль')
        print('2. Файл')
        print('0. Назад')

        while True:
            try:
                print('\nОберіть дію [0-2]:', end = ' ')
                key = int(input())
                break;
            except:
                print('Введіть числове значення!')
        print('*' * 50)

        match key:
            case 0:
                break
            case 1:
                get_console_data()
            case 2:
                get_file_data()