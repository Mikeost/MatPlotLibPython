import os

import matplotlib
import matplotlib.pyplot as plt

import numpy as np

from pylab import *

def simple_graph():
    x = [1, 2, 3, 4]
    y = [1, 4, 2, 3]

    plt.plot(x, y)
    plt.grid()
    plt.show()

def two_graphs():
    x = [1, 2, 3, 4]
    y = [1, 4, 2, 3]
    x2 = range(4)
    y2 = [i + 1 for i in x2]

    plt.plot(x, y, x2, y2)
    plt.grid()
    plt.show()

def bar_graph():
    fig, ax = plt.subplots()
    fruits = ['яблуко', 'апельсин', 'вишня', 'ківі']
    counts = [40, 100, 30, 55]
    barLabels = ['червоний', 'оранжевий', '_червоний', 'зелений']
    barColors = ['tab:red', 'tab:orange', 'tab:red', 'tab:green']

    ax.bar(fruits, counts, label = barLabels, color = barColors)

    ax.set_ylabel('постачання фруктів')
    ax.set_title('Постачаня фруктів за сортом і кольором')
    ax.legend(title = 'Кольори фруктів')
    fig.canvas.manager.set_window_title('Гістограма постачання фруктів')
    plt.show()

def numpy_random_graph():
    np.random.seed(19680801)
    data = {'a': np.arange(50),
            'c': np.random.randint(0, 50, 50),
            'd': np.random.randn(50)}
    data['b'] = data['a'] + 10 * np.random.randn(50)
    data['d'] = np.abs(data['d']) * 100

    fig, ax = plt.subplots(figsize = (5, 2.7), layout = 'constrained')
    ax.scatter('a', 'b', c = 'c', s = 'd', data = data)
    ax.set_xlabel('входження послідовності a')
    ax.set_ylabel('входження послідовності b')
    fig.canvas.manager.set_window_title('Numpy rand послідовності')
    plt.show()

def type_of_graph():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n' + '*' * 50)
        print('\t\t<--Приклади графіків-->\n')
        print('1. Простий лінійний графік')
        print('2. Два лінійних графіка (одна координатна площина)')
        print('3. Гістограма')
        print('4. Графік rand послідовностей (Numpy)')
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
                simple_graph()
            case 2:
                two_graphs()
            case 3:
                bar_graph()
            case 4:
                numpy_random_graph()


        