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

def marker_graph():
    print(cli.bcolors.OKCYAN + '\n' + '*' * 50 + cli.bcolors.ENDC)
    print('\t\t<--Маркери графіка-->\n')
    print('Доступні маркери:')
    print('1. Точка (•)')
    print('2. Піксель (·)')
    print('3. Коло (●)')
    print('4. Трикутник вниз (▼)')
    print('5. Трикутник вгору (▲)')
    print('6. Трикутник вліво (◀)')
    print('7. Трикутник вправо (▶)')
    print('8. Квадрат (◼)')
    print('9. Шестикутник 1 (⬢ )')
    print('10. Шестикутник 2 (⬣ )')
    print('11. Плюс (✚)')
    print('12. Х (✖)')
    print('13. Зірка (★)')
    print('14. Ромб (♦)')
    print('0. Без маркерів\n')

    while True:
        try:
            print('Оберіть номер маркеру [0-14]:', end = ' ')
            key = int(input())
            break
        except:
            print(cli.bcolors.WARNING + 'Введіть числове значення!' + cli.bcolors.ENDC)

    match key:
        case 0:
            return 'None'
        case 1:
            return '.'
        case 2:
            return ','
        case 3:
            return 'o'
        case 4:
            return 'v'
        case 5:
            return '^'
        case 6:
            return '<'
        case 7:
            return '>'
        case 8:
            return 's'
        case 9:
            return 'h'
        case 10:
            return 'H'
        case 11:
            return 'P'
        case 12:
            return 'X'
        case 13:
            return '*'
        case 14:
            return 'd'
        case _:
            return 'None'

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

    color_G = color_graph()
    linestyle_g = linestyle_graph()
    marker_g = marker_graph()

    plt.plot(xList, yList, color_G + linestyle_g, marker = marker_g)
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

            color_G = color_graph()
            linestyle_g = linestyle_graph()
            marker_g = marker_graph()

            plt.plot(xList, yList, color_G + linestyle_g, marker = marker_g)
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