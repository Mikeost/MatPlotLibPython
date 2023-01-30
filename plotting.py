import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import ConnectionPatch

import numpy as np

from pylab import *

import fileinput

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
