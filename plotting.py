import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import ConnectionPatch

import numpy as np

from pylab import *

import random

import tkinter as tk

matplotlib.use("TkAgg")

def marker_graph(key):
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

def linestyle_graph(key):
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

def color_graph(key):
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

def simple_plotting(data, color_G, linestyle_g, marker_g):
    data = data.splitlines()
    x_list = []
    y_list = []

    for line in data:
        line = line.split(' ')
        x_list.append(float(line[0]))
        y_list.append(float(line[1]))

    color_G = color_graph(color_G)
    linestyle_g = linestyle_graph(linestyle_g)
    marker_g = marker_graph(marker_g)

    plt.plot(x_list, y_list, color = color_G, linestyle = linestyle_g, marker = marker_g)
    plt.grid()

    plt.show()

def equation_plotting(equation, x_range, color_G, linestyle_g, marker_g):

    for i in range(len(equation)):
        if equation[i] == '^':
            equation = equation[:i] + '**' + equation[i + 1:]
    x = np.array(x_range)  
    y = eval(equation)

    color_G = color_graph(color_G)
    linestyle_g = linestyle_graph(linestyle_g)
    marker_g = marker_graph(marker_g)

    plt.plot(x, y, color = color_G, linestyle = linestyle_g, marker = marker_g)
    plt.grid()

    plt.show()

def barnsley_fern():
    def f1(x, y):
        return np.array([[0, 0], [0, 0.16]]).dot(np.array([x, y]))


    def f2(x, y):
        return (np.array([[0.85, 0.04], [-0.04, 0.85]]).dot(np.array([x, y]))
                + np.array([0, 1.6]))


    def f3(x, y):
        return (np.array([[0.20, -0.26], [0.23, 0.22]]).dot(np.array([x, y]))
                + np.array([0, 1.6]))


    def f4(x, y):
        return (np.array([[-0.15, 0.28], [0.26, 0.24]]).dot(np.array([x, y]))
                + np.array([0, 0.44]))

    n = 100000

    x, y = [0], [0]

    for _ in range(n):
        r = random.random()
        if r < 0.01:
            dot = f1(x[-1], y[-1])
        elif r < 0.86:
            dot = f2(x[-1], y[-1])
        elif r < 0.93:
            dot = f3(x[-1], y[-1])
        else:
            dot = f4(x[-1], y[-1])
        x.append(dot[0])
        y.append(dot[1])

    plt.plot(x, y, '.', markersize = 2, color = 'g')
    plt.title('Папороть Барнслі')
    plt.tight_layout()
    plt.show()

def dragon_curve():
    def f1(x, y):
        return (1 / sqrt(2)) * np.array([[cos(pi/4), -sin(pi/4)], [sin(pi/4), 
                cos(pi/4)]]).dot(np.array([x, y]))

    def f2(x, y):
        return (1 / sqrt(2)) * np.array([[cos(3*pi/4), -sin(3*pi/4)], [sin(3*pi/4), 
            cos(3*pi/4)]]).dot(np.array([x, y])) + np.array([1, 0])

    n = 50000
    x, y = [0], [0]
    for _ in range(n):
        r = random.random()
        if r <= 0.5:
            dot = f1(x[-1], y[-1])
        else:
            dot = f2(x[-1], y[-1])
        x.append(dot[0])
        y.append(dot[1])

    plt.plot(x, y, '.', markersize = 1, color = 'r')
    plt.title('Крива дракона')
    plt.tight_layout()
    plt.show()

def sierpinsky_triangle_construction():
    def sierpinsky_triangle(n, x, y, c):
        if n != 0:
            xA, yA = x, y
            xB, yB = x + c, y
            xC, yC = x + c / 2, y + c * sqrt(3) / 2
            xE, yE = (xA + xB) / 2, (yA + yB) / 2
            xF, yF = (xB + xC) / 2, (yB + yC) / 2
            xG, yG = (xA + xC) / 2, (yA + yC) / 2
            plt.fill([xE, xF, xG], [yE, yF, yG], 'w')
            sierpinsky_triangle(n - 1, x, y, c / 2)
            sierpinsky_triangle(n - 1, xG, yG, c / 2)
            sierpinsky_triangle(n - 1, xE, yE, c/2)
        else:
            plt.fill([x, x + c, x + c / 2], [y, y, y + c * sqrt(3) / 2], 'b')

    n = 5
    sierpinsky_triangle(n, 0, 0, 10)
    plt.axis("equal")
    plt.title("Трикутник Серпінського")
    plt.tight_layout()
    plt.show()