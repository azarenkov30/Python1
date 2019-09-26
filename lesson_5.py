# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

path_dir = [('dir_' + str(i + 1)) for i in range(9)]

def make_dir(paths):
    dir_path = os.path.join(os.getcwd(), paths)
    try:
        os.mkdir(dir_path)
        print('Папка(-и) успешно сздана(-ы)')
    except:
        print(dir_path + ' - такая директория уже есть')

for i in path_dir:
    make_dir(i)

def remove_dir(paths):
    dir_path = os.path.join(os.getcwd(), paths)
    try:
        os.rmdir(dir_path)
        print('Папка(-и) успешно удалена(-ы)')
    except:
        print(dir_path + ' - такая директория уже удалена')

for i in path_dir:
    remove_dir(i)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# import os

# a = [i for i in os.listdir() if os.path.isdir(i)]
# print(a)


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
#
# import shutil
# print(shutil.copy('lesson_5.py','lesson_5_copy.py'))

