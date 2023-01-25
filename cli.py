import examples
import os

import plotting

logo = ['    __  ___      __  ____  __      __  __    _ __',
        '   /  |/  /___ _/ /_/ __ \/ /___  / /_/ /   (_) /',
        '  / /|_/ / __ `/ __/ /_/ / / __ \/ __/ /   / / __ \\',
        ' / /  / / /_/ / /_/ ____/ / /_/ / /_/ /___/ / /_/ /',
        '/_/  /_/\__,_/\__/_/   /_/\____/\__/_____/_/_.___/ ']

def print_logo():
    for i in range(5):
        print(logo[i])

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    key = 0
    while True:
        print('\n' + '*' * 50)
        print('\t\t<--Головне меню-->\n')
        print('1. Простий графік по точкам')
        print('2. Сферичний графік (!в розробці!)')
        print('3. Приклади графіків')
        print('0. Вийти із програми')
        
        while True:
            try:
                print('\nОберіть дію [0-3]:', end = ' ')
                key = int(input())
                break;
            except:
                print('Введіть числове значення [0-3]!')
        print('*' * 50)

        match key:
            case 0:
                break
            case 1:
                plotting.simple_graph()
            case 3:
                examples.type_of_graph()


        clear_screen()