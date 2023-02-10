import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import ConnectionPatch

import numpy as np

from pylab import *

matplotlib.use("TkAgg")

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

def two_figure():
    t = np.arange(0.0, 2.0, 0.01)
    s1 = np.sin(2 * np.pi * t)
    s2 = np.sin(4 * np.pi * t)

    plt.figure(1)
    plt.subplot(211)
    plt.plot(t, s1)
    plt.subplot(212)
    plt.plot(t, s2)

    plt.show()

def bar_graph():
    fig, ax = plt.subplots()
    fruits = ['яблуко', 'апельсин', 'вишня', 'ківі']
    counts = [40, 100, 30, 55]
    barlabels = ['червоний', 'оранжевий', '_червоний', 'зелений']
    barColors = ['tab:red', 'tab:orange', 'tab:red', 'tab:green']

    ax.bar(fruits, counts, label=barLabels, color=barColors)

    ax.set_ylabel('постачання фруктів')
    ax.set_title('Постачаня фруктів за сортом і кольором')
    ax.legend(title='Кольори фруктів')
    fig.canvas.manager.set_window_title('Гістограма постачання фруктів')
    plt.show()

def basic_pie_graph():
    animals = ['жаби', 'свини', 'собаки', 'ведмеді']
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)

    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, labels=animals, autopct='%1.1f%%', 
           shadow=True, startangle=90)
    ax.axis('equal')
    fig.canvas.manager.set_window_title('Кругова діаграма')
    plt.show()

def pie_lables_graph():
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect='equal'))

    recipe = ['375 g борошна',
              '75 g цукру',
              '250 g вершкового масла',
              '300 g ягід']

    data = [float(x.split()[0]) for x in recipe]
    ingredients = [x.split()[-1] for x in recipe]

    def func(pct, allvals):
        absolute = int(np.round(pct / 100. * np.sum(allvals)))
        return '{:.1f}%\n({:d} g)'.format(pct, absolute)

    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                      textprops=dict(color='w'))

    ax.legend(wedges, ingredients,
              title='Інгредієнти',
              loc='center left',
              bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight='bold')

    ax.set_title('Пиріг')
    fig.canvas.manager.set_window_title('Кругова діаграма з написами')

    plt.show()

def numpy_random_graph():
    np.random.seed(19680801)
    data = {'a': np.arange(50),
            'c': np.random.randint(0, 50, 50),
            'd': np.random.randn(50)}
    data['b'] = data['a'] + 10 * np.random.randn(50)
    data['d'] = np.abs(data['d']) * 100

    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.scatter('a', 'b', c='c', s='d', data=data)
    ax.set_xlabel('входження послідовності a')
    ax.set_ylabel('входження послідовності b')
    fig.canvas.manager.set_window_title('Numpy rand послідовності')
    plt.show()

def animation_graph():
    fig, (axl, axr) = plt.subplots(
        ncols=2,
        sharey=True,
        figsize=(6, 2),
        gridspec_kw=dict(width_ratios=[1, 3], wspace=0)
    )
    axl.set_aspect(1)
    axr.set_box_aspect(1 / 3)
    axr.yaxis.set_visible(False)
    axr.xaxis.set_ticks([0, np.pi, 2 * np.pi], ['0', r'$\pi$', r'$2\pi$'])

    x = np.linspace(0, 2 * np.pi, 50)
    axl.plot(np.cos(x), np.sin(x), 'k', lw=0.3)
    point, = axl.plot(0, 0, 'o')

    sine, = axr.plot(x, np.sin(x))

    con = ConnectionPatch(
        (1, 0),
        (0, 0),
        'data',
        'data',
        axesA=axl,
        axesB=axr,
        color='C0',
        ls='dotted'
    )
    fig.add_artist(con)

    def animate(i):
        pos = np.cos(i), np.sin(i)
        point.set_data(*pos)
        x = np.linspace(0, i, int(i * 25 / np.pi))
        sine.set_data(x, np.sin(x))
        con.xy1 = pos
        con.xy2 = i, pos[1]
        return point, sine, con

    ani = animation.FuncAnimation(
        fig,
        animate,
        interval=50,
        blit=False,
        frames=x,
        repeat_delay=100
    )

    fig.canvas.manager.set_window_title('Анімаційний графік')
    plt.show()

def bar_3d_graph():
    np.random.seed(19680801)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    colors = ['r', 'g', 'b', 'y']
    yticks = [3, 2, 1, 0]
    for c, k in zip(colors, yticks):
        xs = np.arange(20)
        ys = np.random.rand(20)

        cs = [c] * len(xs)
        cs[0] = 'c'

        ax.bar(xs, ys, zs=k, zdir='y', color=cs, alpha=0.8)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.set_yticks(yticks)

    fig.canvas.manager.set_window_title('3D Графік')
    plt.show()