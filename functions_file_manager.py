import os
import sys

def add_dir():
    os.mkdir(input('Введите имя создаваемой папки'))

def del_dir_file():
    file_name = input('Введите имя папки или файла для удаления')
    if os.path.isfile(file_name) :
        os.remove(file_name)
    else:
        if os.path.isdir(file_name) :
            os.rmdir(file_name)
    print('Нет такого фала/папки : ',file_name)

def list_dir():
    print("\033c", end="")
    for root, directories, files in os.walk(os.getcwd()):
        print(root)
    return
def list_only_dirs():
    for root, directories, files in os.walk(os.getcwd()):
        for directory in directories:
            print(directory)

def list_only_files():
    for root, directories, files in os.walk(os.getcwd()):
        for file in files:
            print(file)
def change_dir():
    path_name = input('Введите новый рабочий каталог')
    if os.path.exists(path_name) :
        os.chdir(path_name)
    else:
        print('Такого каталога не существует :',path_name )

def clear_screen():
   print("\n" * 20)