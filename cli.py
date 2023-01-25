import examples
import os

import plotting

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

logo = ['    __  ___      __  ____  __      __  __    _ __',
        '   /  |/  /___ _/ /_/ __ \/ /___  / /_/ /   (_) /',
        '  / /|_/ / __ `/ __/ /_/ / / __ \/ __/ /   / / __ \\',
        ' / /  / / /_/ / /_/ ____/ / /_/ / /_/ /___/ / /_/ /',
        '/_/  /_/\__,_/\__/_/   /_/\____/\__/_____/_/_.___/ ']

def print_logo():
    for i in range(5):
        print(bcolors.OKBLUE + logo[i] + bcolors.ENDC)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    key = 0
    while True:
        print(bcolors.OKCYAN + '\n' + '*' * 50 + bcolors.ENDC)
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
                print(bcolors.WARNING + 'Введіть числове значення [0-3]!' + bcolors.ENDC)
        print(bcolors.OKCYAN + '*' * 50 + bcolors.ENDC)

        match key:
            case 0:
                break
            case 1:
                plotting.simple_graph()
            case 3:
                examples.type_of_graph()


        clear_screen()