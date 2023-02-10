import tkinter as tk
from tkinter import ttk

import numpy as np

import examples

import plotting

win = tk.Tk()

def window_center(_win, width, height):
    screen_width = _win.winfo_screenwidth()
    screen_height = _win.winfo_screenheight()

    x_coordinate = int((screen_width / 2) - (width / 2))
    y_coordinate = int((screen_height / 2) - (height / 2))

    _win.geometry('{}x{}+{}+{}'.format(width, height, x_coordinate, y_coordinate))


def win_init():
    photo = tk.PhotoImage(file='media/logo.png')
    win.iconphoto(False, photo)
    win.title('MatPlotLibPython')

    window_width = 600
    window_height = 500

    win.resizable(False, False)

    window_center(win, window_width, window_height)

    # Labels
    title_label = tk.Label(win, text='MatPlotLibPython',
                           font=('Arial', 30, 'bold'),
                           pady=20)

    title_label.pack()

    # Buttons 
    simple_graph_button = tk.Button(win, text='Простий графік по точкам',
                                    command=simple_graph_page, width=20,
                                    height=2)

    equation_graph_button = tk.Button(win, text='Графік за рівнянням',
                                      command=equation_graph_page, 
                                      width=20,
                                      height=2)

    fractal_graph_button = tk.Button(win, text='Фрактали',
                                     command=fractal_graph_page, 
                                     width=20,
                                     height=2)

    examples_button = tk.Button(win, text='Приклади графіків',
                                command=examples_page, width=20,
                                height=2)

    exit_button = tk.Button(win, text='Вийти з програми',
                            command=exit, width=20,
                            height=2)

    simple_graph_button.pack(pady=15)
    equation_graph_button.pack(pady=15)
    fractal_graph_button.pack(pady=15)
    examples_button.pack(pady=15)
    exit_button.pack(pady=30)

    win.mainloop()

def simple_graph_page():

    def close():
        simple_graph_win.destroy()
        simple_graph_win.update()

    def browse_files():
        filename = tk.filedialog.askopenfilename(initialdir='/', title='Оберіть файл',
                                                 filetypes=(('Text files',
                                                             '*.txt'),
                                                            ('all files',
                                                             '*.*')))

        if not filename:
            return

        with open(filename, 'r') as data:
            data = data.read()

        return data

    def select_var():
        var = input_var.get()
        if var == 0:
            data = coord_lists.get('1.0', 'end-1c')
            if not data:
                return
            plotting.simple_plotting(data, colors_combobox.current(), linestyles_combobox.current(), markers_combobox.current())
        elif var == 1:
            data = browse_files()
            if not data:
                return
            plotting.simple_plotting(data, colors_combobox.current(), linestyles_combobox.current(), markers_combobox.current())
        else:
            tk.messagebox.showinfo(title='Помилка!', message='Оберіть варіант введення!')


    simple_graph_win = tk.Toplevel(win)
    photo = tk.PhotoImage(file='media/logo.png')
    simple_graph_win.iconphoto(False, photo)
    simple_graph_win.title('Простий графік по точкам')

    window_width = 500
    window_height = 650

    simple_graph_win.resizable(False, False)

    window_center(simple_graph_win, window_width, window_height)

    # Labels
    title_label = tk.Label(simple_graph_win, text='Простий графік по точкам',
                           font=('Arial', 30, 'bold'),
                           pady=20, padx=50
                           ).grid(column=0, row=0, columnspan=7, sticky='n')

    # Input
    input_var = tk.IntVar()

    tk.Radiobutton(simple_graph_win, text='Текстове введення', variable=input_var, 
                   value=0, pady=20).grid(column=1, row=1, columnspan=2)

    coord_lists = tk.Text(simple_graph_win, width=20, height=4)
    coord_lists.grid(column=1, row=2, columnspan=2)


    filename = None
    tk.Radiobutton(simple_graph_win, text='Введення із файлу', variable=input_var, 
                   value=1, pady=20).grid(column=4, row=1, columnspan=2)

    # Color
    graph_color_label = tk.Label(simple_graph_win, text='Оберіть колір графіку:', anchor='nw',
                                 font=('Arial', 15, 'normal'), pady=20, padx=50).grid(column=0, row=3,
                                 columnspan=7)

    colors = ('Чорний', 'Синій', 'Зелений', 'Червоний', 'Блакитний', 'Пурпуровий', 'Жовтий')

    colors_combobox = ttk.Combobox(simple_graph_win, values=colors)
    colors_combobox.current(0)
    colors_combobox.grid(column=0, row=4, columnspan=7)

    # Linestyle
    linestyle_label = tk.Label(simple_graph_win, text='Оберіть тип лінії:', anchor='nw',
                               font=('Arial', 15, 'normal'), pady=20, padx=50).grid(column=0, row=5,
                               columnspan=7)

    linestyles = ('Суцільна лінія(за замовчуванням)', 'Пунктирна лінія', 'Довга пунктирна лінія', 'Штрихпунктирна лінія')

    linestyles_combobox = ttk.Combobox(simple_graph_win, values=linestyles)
    linestyles_combobox.current(0)
    linestyles_combobox.grid(column=0, row=6, columnspan=7)

    # Marker
    marker_label = tk.Label(simple_graph_win, text='Оберіть тип маркерів:', anchor='nw',
                            font=('Arial', 15, 'normal'), pady=20, padx=50).grid(column=0, row=7,
                            columnspan=7)

    markers = ('Без маркерів', '•', '·', '●', '▼', '▲', '◀', '▶', '◼', '⬢', '⬣', '✚', '✖', '★', '♦')

    markers_combobox = ttk.Combobox(simple_graph_win, values=markers)
    markers_combobox.current(0)
    markers_combobox.grid(column=0, row=8, columnspan=7)

    # Buttons 
    plotting_button = tk.Button(simple_graph_win, text='Побудувати графік',
                                command=select_var, 
                                width=20,
                                height=2).grid(column=0, row=9, columnspan=7, pady=(30, 10))


    back_button = tk.Button(simple_graph_win, text='Назад',
                            command=close, width=20,
                            height=2).grid(column=0, row=10, columnspan=7)

def fractal_graph_page():

    def close():
        fractal_win.destroy()
        fractal_win.update()

    def plotting_graph():
        match type_of_fractal_combobox.current():
            case 0:
                plotting.barnsley_fern()
            case 1:
                plotting.dragon_curve()
            case 2:
                plotting.sierpinsky_triangle_construction()


    fractal_win = tk.Toplevel(win)
    photo = tk.PhotoImage(file='media/logo.png')
    fractal_win.iconphoto(False, photo)
    fractal_win.title('Фрактали')

    window_width = 500
    window_height = 350

    fractal_win.resizable(False, False)

    window_center(fractal_win, window_width, window_height)

    # Labels
    title_label = tk.Label(fractal_win, text='Фрактали',
                           font=('Arial', 30, 'bold'),
                           pady=20).pack()

    type_of_fractal_title = tk.Label(fractal_win, text='Оберіть тип фракакталу:', anchor='nw',
                                 font=('Arial', 15, 'normal'), pady=20, padx=50).pack()

    types_of_fractal = ('Папороть Барнслі', 'Крива дракона', 'Трикутник Серпінського')

    type_of_fractal_combobox = ttk.Combobox(fractal_win, values=types_of_fractal)
    type_of_fractal_combobox.current(0)
    type_of_fractal_combobox.pack()

    plotting_button = tk.Button(fractal_win, text='Побудувати графік',
                                command=plotting_graph, width=20,
                                height=2).pack(pady=15)

    back_button = tk.Button(fractal_win, text='Назад',
                            command=close, width=20,
                            height=2).pack(pady=15)

def examples_page():

    def close():
        examples_win.destroy()
        examples_win.update()

    examples_win = tk.Toplevel(win)
    photo = tk.PhotoImage(file='media/logo.png')
    examples_win.iconphoto(False, photo)
    examples_win.title('Приклади графіків')

    window_width = 600
    window_height = 650

    examples_win.resizable(False, False)

    window_center(examples_win, window_width, window_height)

    # Labels
    title_label = tk.Label(examples_win, text='Приклади графіків',
                           font=('Arial', 30, 'bold'),
                           pady=20).pack()

    # Buttons 
    simple_graph_button = tk.Button(examples_win, text='Простий лінійний графік',
                                    command=examples.simple_graph, width=40,
                                    height=2).pack(pady=5)

    two_graphs_button = tk.Button(examples_win, text='Два лінійних графіка (одна координатна площина)',
                                  command=examples.two_graphs, width=40,
                                  height=2).pack(pady=5)

    two_figure_button = tk.Button(examples_win, text='Два лінійних графіка на окремих коорд. площинах',
                                  command=examples.two_figure, width=40,
                                  height=2).pack(pady=5)

    bar_graph_button = tk.Button(examples_win, text='Гістограма',
                                 command=examples.bar_graph, width=40,
                                 height=2).pack(pady=5)

    basic_pie_graph_button = tk.Button(examples_win, text='Кругова діаграма',
                                       command=examples.basic_pie_graph, width=40,
                                       height=2).pack(pady=5)

    pie_lables_graph_button = tk.Button(examples_win, text='Кругова діаграма з написами',
                                        command=examples.pie_lables_graph, width=40,
                                        height=2).pack(pady=5)

    numpy_random_graph_button = tk.Button(examples_win, text='Графік rand послідовностей (Numpy)',
                                          command=examples.numpy_random_graph, width=40,
                                          height=2).pack(pady=5)

    animation_graph_button = tk.Button(examples_win, text='Анімація графіка',
                                       command=examples.animation_graph, width=40,
                                       height=2).pack(pady=5)

    bar_3d_graph_button = tk.Button(examples_win, text='3D Гістограма',
                                    command=examples.bar_3d_graph, width=40,
                                    height=2).pack(pady=5)

    back_button = tk.Button(examples_win, text='Назад',
                            command=close, width=40,
                            height=2).pack(pady=15)

def equation_graph_page():

    def close():
        equation_graph_win.destroy()
        equation_graph_win.update()

    def plotting_graph():
        plotting.equation_plotting(equation.get('1.0', 'end-1c'), np.arange(int(x_left.get('1.0', 'end-1c')), int(x_right.get('1.0', 'end-1c')) + 1), 
                                   colors_combobox.current(), linestyles_combobox.current(), markers_combobox.current())


    equation_graph_win = tk.Toplevel(win)
    photo = tk.PhotoImage(file='media/logo.png')
    equation_graph_win.iconphoto(False, photo)
    equation_graph_win.title('Графік за рівнянням')

    window_width = 400
    window_height = 600

    equation_graph_win.resizable(False, False)

    window_center(equation_graph_win, window_width, window_height)

    title_label = tk.Label(equation_graph_win, text='Графік за рівнянням',
                           font=('Arial', 30, 'bold'),
                           pady=20, padx=50
                           ).grid(column=0, row=0, columnspan=5, sticky='n')

    y_label = tk.Label(equation_graph_win, text='y =',
                       font=('Arial', 15, 'normal'), pady=10
                       ).grid(column=0, row=1, columnspan=1, sticky='e')

    equation = tk.Text(equation_graph_win, width=18, height=1, padx=0)
    equation.grid(column=2, row=1, columnspan=2, sticky='w')

    x_label = tk.Label(equation_graph_win, text='Діапазон x:',
                       font=('Arial', 15, 'normal'), pady=10
                       ).grid(column=0, row=2, columnspan=1, sticky='e')

    x_left = tk.Text(equation_graph_win, width=5, height=1, padx=0)
    x_left.grid(column=2, row=2, columnspan=1, sticky='w')

    x_right = tk.Text(equation_graph_win, width=5, height=1, padx=0)
    x_right.grid(column=3, row=2, columnspan=1, sticky='w')

    # Color
    graph_color_label = tk.Label(equation_graph_win, text='Оберіть колір графіку:', anchor='nw',
                                 font=('Arial', 15, 'normal'), pady=20, padx=50).grid(column=0, row=3,
                                 columnspan=5)

    colors = ('Чорний', 'Синій', 'Зелений', 'Червоний', 'Блакитний', 'Пурпуровий', 'Жовтий')

    colors_combobox = ttk.Combobox(equation_graph_win, values=colors)
    colors_combobox.current(0)
    colors_combobox.grid(column=0, row=4, columnspan=5)

    # Linestyle
    linestyle_label = tk.Label(equation_graph_win, text='Оберіть тип лінії:', anchor='nw',
                               font=('Arial', 15, 'normal'), pady=20, padx=50).grid(column=0, row=5,
                               columnspan=5)

    linestyles = ('Суцільна лінія(за замовчуванням)', 'Пунктирна лінія', 'Довга пунктирна лінія', 'Штрихпунктирна лінія')

    linestyles_combobox = ttk.Combobox(equation_graph_win, values=linestyles)
    linestyles_combobox.current(0)
    linestyles_combobox.grid(column=0, row=6, columnspan=5)

    # Marker
    marker_label = tk.Label(equation_graph_win, text='Оберіть тип маркерів:', anchor='nw',
                            font=('Arial', 15, 'normal'), pady=20, padx=50).grid(column=0, row=7,
                            columnspan=5)

    markers = ('Без маркерів', '•', '·', '●', '▼', '▲', '◀', '▶', '◼', '⬢', '⬣', '✚', '✖', '★', '♦')

    markers_combobox = ttk.Combobox(equation_graph_win, values=markers)
    markers_combobox.current(0)
    markers_combobox.grid(column=0, row=8, columnspan=5)

    # Buttons 
    plotting_button = tk.Button(equation_graph_win, text='Побудувати графік',
                                command=plotting_graph, 
                                width=20,
                                height=2).grid(column=0, row=9, columnspan=5, pady=(30, 10))


    back_button = tk.Button(equation_graph_win, text='Назад',
                            command=close, width=20,
                            height=2).grid(column=0, row=10, columnspan=5)

if __name__ == '__main__':
    win_init()