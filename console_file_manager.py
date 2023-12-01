

from functions_file_manager import *
sys.path.append('/console_games')
from console_games.game_count import *
from console_games.game_victorina import victorina

while True:
    print("\n" * 2)
    print('1. Создать папку',
    '2. Удалить файл/папку',
    '3. Копировать файл/папку',
    '4. Просмотр содержимого рабочей директории',
    '5. Посмотреть только папки;')
    print('6. Посмотреть только файлы',
    '7. Просмотр информации об операционной системе',
    '8. Сздатель программы',
    '9. Играть в викторину',
    '10. Мой банковский счет')
    print('11. Сменить рабочую директорию',
    '12. Сохранить содержимое рабочей директории в файл',
    '13. выход')

    choice = input('Выберите пункт меню ')
    if choice == '1':
        pass
        add_dir()
    elif choice == '2':
        file_name = input('Введите имя папки или файла для удаления')
        if del_dir_file(file_name) == False:
            print('Нет такого файла/папки или папка не пустая: ', file_name)

    elif choice == '3':
        pass
        file_copy()
    elif choice == '4':
        print("\033c", end="")
        for i in list_dir():
            print(i)
    elif choice == '5':
        print("\033c", end="")
        for i in list_dir('dir'):
            print(i)
    elif choice == '6':
        print("\033c", end="")
        for i in list_dir('file'):
            print(i)
    elif choice == '7':
        print('\n\nОперационная система : ',(sys.platform))
        pass
    elif choice == '8':
        print('\n\nСтудент RispomMai')
        pass
    elif choice == '9':
        victorina()
        pass
    elif choice == '10':
        history_pay = []
        game_count()
        pass
    elif choice == '11':
        path_name = input('Введите новый рабочий каталог')
        if change_dir(path_name) == False:
            print('Такого каталога не существует :', path_name)
        pass
    elif choice == '12':
        listdirfile()
        print('\nСодержимое рабочей директории сохранено в файле listdir.txt\n')
        pass
    elif choice == '13':

        break
    else:
        print('Неверный пункт меню')