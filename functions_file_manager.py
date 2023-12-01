import os
import sys
import shutil

FILENAME_FOR_LISTDIR = 'listdir.txt '

def add_dir():
    os.mkdir(input('Введите имя создаваемой папки'))

def del_dir_file(file_name):
    #file_name = input('Введите имя папки или файла для удаления')
    if os.path.isfile(file_name) :
        os.remove(file_name)
        return True
    else:
        if os.path.isdir(file_name):
            if len(os.listdir(file_name)) == 0:
                os.rmdir(file_name)
            return True
        else:
            return False

def listdirfile():
    with open(FILENAME_FOR_LISTDIR, 'w') as f:
        tree = list(os.walk(os.getcwd()))
        f.write('files: ')
        for file in tree[0][2]:
            f.write(file)
            f.write(',')
        f.write('\n\n')
        f.write('dirs: ')
        for dir in tree[0][1]:
            f.write(dir)
            f.write(',')




def list_dir(view="All"):
    str_view = []
    for root, directories, files in os.walk(os.getcwd()):
        if view == 'All':
            str_view.append(root)
        elif view == 'dir':
            for directory in directories:
                str_view.append(directory)
        else:
            for file in files:
                str_view.append(file)
    return(str_view)

def change_dir(path_name):
    if os.path.exists(path_name) :
        os.chdir(path_name)
        return True
    else:
        return False


def file_copy():
    copy_path = os.getcwd()
    file_name1 = input('Введите имя файла для копирования')

    if os.path.isfile(file_name1):
        file_name_2 = input('Введите имя нового файла')
        copy_file = shutil.copy2(os.path.join(copy_path, file_name1), os.path.join(copy_path, file_name_2))
        print(file_name1)
    else:
        print('Нет такого фала/папки : ',file_name1)





