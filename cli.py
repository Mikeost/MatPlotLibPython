import examples
import os

logo = ['    __  ___      __  ____  __      __  __    _ __',
        '   /  |/  /___ _/ /_/ __ \/ /___  / /_/ /   (_) /',
        '  / /|_/ / __ `/ __/ /_/ / / __ \/ __/ /   / / __ \\',
        ' / /  / / /_/ / /_/ ____/ / /_/ / /_/ /___/ / /_/ /',
        '/_/  /_/\__,_/\__/_/   /_/\____/\__/_____/_/_.___/ ']

def printLogo():
        for i in range(5):
                print(logo[i])

def menu():
    key = 0
    while True:
        print('\n' + '*' * 50)
        print('1. Простий графік')
        print('2. Сферичний графік')
        print('3. Приклади графіків')
        print('0. Вийти із програми')
        print('\nОберіть варіант:')
        while True:
            try:
                key = int(input())
                break;
            except:
                print('Введіть числове значення!!!')
        print('*' * 50)

        if key == 0:
            break
        elif key == 3:
            examples.simple()


        os.system('cls' if os.name == 'nt' else 'clear')