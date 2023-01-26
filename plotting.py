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

def linestyle_graph():
    print(cli.bcolors.OKCYAN + '\n' + '*' * 50 + cli.bcolors.ENDC)
    print('\t\t<--Стиль ліній-->\n')
    print('Доступні стилі:')
    print('1. Пунктирна лінія')
    print('2. Довга пунктирна лінія')
    print('3. Штрихпунктирна лінія')
    print('0. Суцільна лінія(за замовчуванням)\n')

    while True:
        try:
            print('Оберіть номер стилю [0-3]:', end = ' ')
            key = int(input())
            break
        except:
            print(cli.bcolors.WARNING + 'Введіть числове значення!' + cli.bcolors.ENDC)

    match key:
        case 0:
            return '-'
        case 1:
            return ':'
        case 2:
            return '--'
        case 3:
            return '-.'
        case _:
            return '-'


def color_graph():
    print('\t\t<--Колір графіка-->\n')
    print('Доступні кольори:')
    print('1. Синій')
    print('2. Зелений')
    print('3. Червоний')
    print('4. Блакитний')
    print('5. Пурпуровий')
    print('6. Жовтий')
    print('0. Чорний(за замовчуванням)\n')

    while True:
        try:
            print('Оберіть номер кольору [0-6]:', end = ' ')
            key = int(input())
            break
        except:
            print(cli.bcolors.WARNING + 'Введіть числове значення!' + cli.bcolors.ENDC)

    match key:
        case 0:
            return 'k'
        case 1:
            return 'b'
        case 2:
            return 'g'
        case 3:
            return 'r'
        case 4:
            return 'c'
        case 5:
            return 'm'
        case 6:
            return 'y'
        case _:
            return 'k'

def get_console_data():
    while True:
        try:
            print('Введіть кількість точок:', end = ' ')
            count = int(input())
            break
        except:
            print(cli.bcolors.WARNING + 'Введіть числове значення!' + cli.bcolors.ENDC)
    
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
                print(cli.bcolors.WARNING + 'Введіть числове значення!' + cli.bcolors.ENDC)

        while True:
            try:
                print('Y' + str(i) + ':', end = ' ')
                y = float(input())
                yList.append(y)
                break
            except:
                print(cli.bcolors.WARNING + 'Введіть числове значення!' + cli.bcolors.ENDC)

    print(xList)
    print(yList)
    print(cli.bcolors.OKCYAN + '*' * 50 + cli.bcolors.ENDC)

    colorG = color_graph()
    linestyle_g = linestyle_graph()

    plt.plot(xList, yList, colorG + linestyle_g)
    plt.grid()
    plt.show()

def get_file_data():
    print(cli.bcolors.OKGREEN + '\nФайл повинен мати таку структуру:\n',
          'x0 y0\n',
          'x1 y1\n',
          'xn-1 yn-1\n',
          'Де x & y - координати точок.\n',
          'Наприклад:\n',
          '1 1\n',
          '2 4\n',
          '3 2\n',
          '4 3\n' + cli.bcolors.ENDC)

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

            print(cli.bcolors.OKCYAN + '*' * 50 + cli.bcolors.ENDC)

            colorG = color_graph()
            linestyle_g = linestyle_graph()

            plt.plot(xList, yList, colorG + linestyle_g)
            plt.grid()
            plt.show()

            return

        except IOError:
            print(cli.bcolors.WARNING + 'Невірна назва файлу!' + cli.bcolors.ENDC)


def simple_graph():
    while True:
        cli.clear_screen()
        print(cli.bcolors.OKCYAN + '\n' + '*' * 50 + cli.bcolors.ENDC)
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
                print(cli.bcolors.WARNING + 'Введіть числове значення!' + cli.bcolors.ENDC)
        print(cli.bcolors.OKCYAN + '*' * 50 + cli.bcolors.ENDC)

        match key:
            case 0:
                break
            case 1:
                get_console_data()
            case 2:
                get_file_data()