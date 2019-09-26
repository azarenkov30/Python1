import os
from lesson_5 import make_dir, remove_dir

def main():
    while True:
        print('''1 - Перейти в папку
2 - Посмотреть содержимое текущей папки
3 - Удалить папку
4 - Создать папку
q - для выхода из программы''')
        task = input()

        if task == 'q':
            print('До свидания.')
            break

        elif task == '1':
            dirname = input('Введите имя нужной дериктории: ')
            try:
                os.chdir(dirname)
                cwd = os.getcwd()
                print('Вы успешно перешли в ', cwd)
            except:
                print('Не верно указан путь: ', dirname)

        elif task == '2':
            now_dir = [i for i in os.listdir()]
            print(now_dir)

        elif task == '3':
            dirname = input('Введите имя папки: ')
            if remove_dir(dirname):
                print('{}'.format(dirname))

        elif task == '4':
            dirname = input('Введите имя папки: ')
            if make_dir(dirname):
                print('{}'.format(dirname))


main()