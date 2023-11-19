
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
    '12. выход')

    choice = input('Выберите пункт меню ')
    if choice == '1':
        pass
        add_dir()
    elif choice == '2':
        pass
        del_dir_file()
    elif choice == '3':
        pass
        list_dir()
    elif choice == '4':
        list_dir()
        pass
    elif choice == '5':
        list_only_dirs()
        pass
    elif choice == '6':
        list_only_files()
        pass
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
        change_dir()
        pass
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')