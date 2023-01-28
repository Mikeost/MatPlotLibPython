import tkinter as tk

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
    photo = tk.PhotoImage(file = 'media/logo.png')
    win.iconphoto(False, photo)
    #win.config(bg = 'white')
    win.title('MatPlotLibPython')

    window_width = 600
    window_height = 500

    win.resizable(False, False)

    window_center(win, window_width, window_height)

    # Labels
    title_label = tk.Label(win, text = 'MatPlotLibPython',
                           font = ('Arial', 30, 'bold'),
                           pady = 20)

    title_label.pack()

    # Buttons 
    simple_graph_button = tk.Button(win, text = 'Простий графік по точкам',
                                    command = simple_graph_page, width = 20,
                                    height = 2,)

    bare_graph_button = tk.Button(win, text = 'Гістограма(в розробці)',
                                  #command = , 
                                  width = 20,
                                  height = 2,)

    examples_button = tk.Button(win, text = 'Приклади графіків',
                                command = examples_page, width = 20,
                                height = 2,)

    exit_button = tk.Button(win, text = 'Вийти з програми',
                            command = exit, width = 20,
                            height = 2,)

    simple_graph_button.pack(pady = 15)
    bare_graph_button.pack(pady = 15)
    examples_button.pack(pady = 15)
    exit_button.pack(pady = 30)

    win.mainloop()

def simple_graph_page():

    def close():
        simple_graph_win.destroy()
        simple_graph_win.update()

    def browse_files():
        filename = tk.filedialog.askopenfilename(initialdir = '/', title = 'Оберіть файл',
                                                 filetypes = (('Text files',
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
            plotting.simple_plotting(data, color_var.get(), linestyle_var.get(), marker_var.get())
        elif var == 1:
            data = browse_files()
            if not data:
                return
            plotting.simple_plotting(data, color_var.get(), linestyle_var.get(), marker_var.get())
        else:
            tk.messagebox.showinfo(title = 'Помилка!', message = 'Оберіть варіант введення!')


    simple_graph_win = tk.Toplevel(win)
    photo = tk.PhotoImage(file = 'media/logo.png')
    simple_graph_win.iconphoto(False, photo)
    simple_graph_win.title('Простий графік по точкам')

    window_width = 500
    window_height = 775

    simple_graph_win.resizable(False, False)

    window_center(simple_graph_win, window_width, window_height)

    # Labels
    title_label = tk.Label(simple_graph_win, text = 'Простий графік по точкам',
                       #bg = 'white', fg = 'black',
                       font = ('Arial', 30, 'bold'),
                       pady = 20, padx = 50
                       ).grid(column = 0, row = 0, columnspan = 7, sticky = 'n')

    # Input
    input_var = tk.IntVar()

    tk.Radiobutton(simple_graph_win, text = 'Текстове введення', variable = input_var, 
                                 value = 0, pady = 20).grid(column = 1, row = 1, columnspan = 2)

    coord_lists = tk.Text(simple_graph_win, width = 20, height = 4)
    coord_lists.grid(column = 1, row = 2, columnspan = 2)


    filename = None
    tk.Radiobutton(simple_graph_win, text = 'Введення із файлу', variable = input_var, 
                                 value = 1, pady = 20).grid(column = 4, row = 1, columnspan = 2)

    # Color
    graph_color_label = tk.Label(simple_graph_win, text = 'Оберіть колір графіку:', anchor = 'nw',
                                 font = ('Arial', 15, 'normal'), pady = 20, padx = 50).grid(column = 0, row = 4,
                                 columnspan = 7)

    color_var = tk.IntVar()

    tk.Radiobutton(simple_graph_win, text = 'Чорний', variable = color_var, 
                                 value = 0).grid(column = 1, row = 5)
    tk.Radiobutton(simple_graph_win, text = 'Синій', variable = color_var, 
                                 value = 1).grid(column = 2, row = 5, columnspan = 3)
    tk.Radiobutton(simple_graph_win, text = 'Зелений', variable = color_var, 
                                 value = 2).grid(column = 5, row = 5)
    tk.Radiobutton(simple_graph_win, text = 'Червоний', variable = color_var, 
                                 value = 3).grid(column = 1, row = 6)
    tk.Radiobutton(simple_graph_win, text = 'Блакитний', variable = color_var, 
                                 value = 4).grid(column = 2, row = 6, columnspan = 3)
    tk.Radiobutton(simple_graph_win, text = 'Пурпуровий', variable = color_var, 
                                 value = 5).grid(column = 5, row = 6)
    tk.Radiobutton(simple_graph_win, text = 'Жовтий', variable = color_var, 
                                 value = 6).grid(column = 2, row = 7, columnspan = 3)

    # Linestyle
    linestyle_label = tk.Label(simple_graph_win, text = 'Оберіть тип лінії:', anchor = 'nw',
                                 font = ('Arial', 15, 'normal'), pady = 20, padx = 50).grid(column = 0, row = 8,
                                 columnspan = 7)

    linestyle_var = tk.IntVar()

    tk.Radiobutton(simple_graph_win, text = 'Суцільна лінія(за замовчуванням)', variable = linestyle_var, 
                                 value = 0).grid(column = 0, row = 9, columnspan = 7)
    tk.Radiobutton(simple_graph_win, text = 'Пунктирна лінія', variable = linestyle_var, 
                                 value = 1).grid(column = 0, row = 10, columnspan = 7)
    tk.Radiobutton(simple_graph_win, text = 'Довга пунктирна лінія', variable = linestyle_var, 
                                 value = 2).grid(column = 0, row = 11, columnspan = 7)
    tk.Radiobutton(simple_graph_win, text = 'Штрихпунктирна лінія', variable = linestyle_var, 
                                 value = 3).grid(column = 0, row = 12, columnspan = 7)

    # Marker
    marker_label = tk.Label(simple_graph_win, text = 'Оберіть тип маркерів:', anchor = 'nw',
                                 font = ('Arial', 15, 'normal'), pady = 20, padx = 50).grid(column = 0, row = 13,
                                 columnspan = 7)

    marker_var = tk.IntVar()

    tk.Radiobutton(simple_graph_win, text = 'Без маркерів', variable = marker_var, 
                                 value = 0).grid(column = 1, row = 14)
    tk.Radiobutton(simple_graph_win, text = '•', variable = marker_var, 
                                 value = 1).grid(column = 2, row = 14)
    tk.Radiobutton(simple_graph_win, text = '·', variable = marker_var, 
                                 value = 2).grid(column = 3, row = 14)
    tk.Radiobutton(simple_graph_win, text = '●', variable = marker_var, 
                                 value = 3).grid(column = 4, row = 14)
    tk.Radiobutton(simple_graph_win, text = '▼', variable = marker_var, 
                                 value = 4).grid(column = 5, row = 14)
    tk.Radiobutton(simple_graph_win, text = '▲', variable = marker_var, 
                                 value = 5).grid(column = 1, row = 15)
    tk.Radiobutton(simple_graph_win, text = '◀', variable = marker_var, 
                                 value = 6).grid(column = 2, row = 15)
    tk.Radiobutton(simple_graph_win, text = '▶', variable = marker_var, 
                                 value = 7).grid(column = 3, row = 15)
    tk.Radiobutton(simple_graph_win, text = '◼', variable = marker_var, 
                                 value = 8).grid(column = 4, row = 15)
    tk.Radiobutton(simple_graph_win, text = '⬢', variable = marker_var, 
                                 value = 9).grid(column = 5, row = 15)
    tk.Radiobutton(simple_graph_win, text = '⬣', variable = marker_var, 
                                 value = 10).grid(column = 1, row = 16)
    tk.Radiobutton(simple_graph_win, text = '✚', variable = marker_var, 
                                 value = 11).grid(column = 2, row = 16)
    tk.Radiobutton(simple_graph_win, text = '✖', variable = marker_var, 
                                 value = 12).grid(column = 3, row = 16)
    tk.Radiobutton(simple_graph_win, text = '★', variable = marker_var, 
                                 value = 13).grid(column = 4, row = 16)
    tk.Radiobutton(simple_graph_win, text = '♦', variable = marker_var, 
                                 value = 14).grid(column = 5, row = 16)


    # Buttons 
    plotting_button = tk.Button(simple_graph_win, text = 'Побудувати графік',
                                command = select_var, width = 20,
                                height = 2).grid(column = 0, row = 17, columnspan = 7, pady = (30, 10))


    back_button = tk.Button(simple_graph_win, text = 'Назад',
                            command = close, width = 20,
                            height = 2).grid(column = 0, row = 18, columnspan = 7)

def examples_page():

    def close():
        examples_win.destroy()
        examples_win.update()

    examples_win = tk.Toplevel(win)
    photo = tk.PhotoImage(file = 'media/logo.png')
    examples_win.iconphoto(False, photo)
    examples_win.title('Приклади графіків')

    window_width = 600
    window_height = 650

    examples_win.resizable(False, False)

    window_center(examples_win, window_width, window_height)

    # Labels
    title_label = tk.Label(examples_win, text = 'Приклади графіків',
                           font = ('Arial', 30, 'bold'),
                           pady = 20).pack()

    # Buttons 
    simple_graph_button = tk.Button(examples_win, text = 'Простий лінійний графік',
                                    command = examples.simple_graph, width = 40,
                                    height = 2).pack(pady = 5)

    two_graphs_button = tk.Button(examples_win, text = 'Два лінійних графіка (одна координатна площина)',
                                  command = examples.two_graphs, width = 40,
                                  height = 2).pack(pady = 5)

    two_figure_button = tk.Button(examples_win, text = 'Два лінійних графіка на окремих коорд. площинах',
                                  command = examples.two_figure, width = 40,
                                  height = 2).pack(pady = 5)

    bar_graph_button = tk.Button(examples_win, text = 'Гістограма',
                                 command = examples.bar_graph, width = 40,
                                 height = 2).pack(pady = 5)

    basic_pie_graph_button = tk.Button(examples_win, text = 'Кругова діаграма',
                                 command = examples.basic_pie_graph, width = 40,
                                 height = 2).pack(pady = 5)

    pie_lables_graph_button = tk.Button(examples_win, text = 'Кругова діаграма з написами',
                                 command = examples.pie_lables_graph, width = 40,
                                 height = 2).pack(pady = 5)

    numpy_random_graph_button = tk.Button(examples_win, text = 'Графік rand послідовностей (Numpy)',
                                 command = examples.numpy_random_graph, width = 40,
                                 height = 2).pack(pady = 5)

    animation_graph_button = tk.Button(examples_win, text = 'Анімація графіка',
                                 command = examples.animation_graph, width = 40,
                                 height = 2).pack(pady = 5)

    bar_3d_graph_button = tk.Button(examples_win, text = '3D Гістограма',
                                 command = examples.bar_3d_graph, width = 40,
                                 height = 2).pack(pady = 5)

    back_button = tk.Button(examples_win, text = 'Назад',
                            command = close, width = 40,
                            height = 2).pack(pady = 15)

if __name__ == '__main__':
    win_init()