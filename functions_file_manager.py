import os
import sys
import shutil


def add_dir():
    os.mkdir(input('Введите имя создаваемой папки'))

def del_dir_file():
    file_name = input('Введите имя папки или файла для удаления')
    if os.path.isfile(file_name) :
        os.remove(file_name)
    else:
        if os.path.isdir(file_name) :
            os.rmdir(file_name)
        else:
            print('Нет такого фала/папки : ',file_name)

def list_dir(view="All"):
    print("\033c", end="")
    for root, directories, files in os.walk(os.getcwd()):
        if view == 'All':
            print(root)
        elif view == 'dir':
            for directory in directories:
                print(directory)
        else:
            for file in files:
                print(file)
    return

def change_dir():
    path_name = input('Введите новый рабочий каталог')
    if os.path.exists(path_name) :
        os.chdir(path_name)
    else:
        print('Такого каталога не существует :',path_name )

def file_copy():
    copy_path = os.getcwd()
    file_name1 = input('Введите имя файла для копирования')

    if os.path.isfile(file_name1):
        file_name_2 = input('Введите имя нового файла')
        copy_file = shutil.copy2(os.path.join(copy_path, file_name1), os.path.join(copy_path, file_name_2))
        print(file_name1)
    else:
        print('Нет такого фала/папки : ',file_name1)





