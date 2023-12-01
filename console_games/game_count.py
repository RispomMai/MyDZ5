import os

FILENAME_FOR_COUNT = 'count.bin'
FILENAME_FOR_HISTORY = 'history.txt'

def read_count(filename):
    mc = 0
    if os.path.isfile(filename):
        with open(filename, 'r+b') as f:
            my_c = f.readline(4)
        return(mc.from_bytes(my_c, byteorder='big'))
    else:
        return(0)

def write_count(filename,count):
    with open(filename, 'w+b') as f:
        f.seek(0)
        f.write(count.to_bytes(4, byteorder='big'))


def read_history(filename):
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            result = f.read()
        result = result.rstrip(';')
        return(result.split(';'))
    else:
        return([])

def write_history(filename,history):
    with open(filename, 'w') as f:
        for i in history:
            if i != '':
                f.write(i)
                f.write(';')

def add_count(count,add_count):
    count += add_count
        # int(input('Введите сумму на которую хотите пополнить счет :')))
    return(count)

def pay_count(count,history_pay):
    pokupka = int(input('Введите сумму покупки :'))
    if count > pokupka:
        name_pokupka = input('Введите название покупки :')
        history_pay.append(name_pokupka+ ' - '+str(pokupka))
        return(count - pokupka)
    else:
        print('На счете недостаточно средств')
        print('История ваших покупок :')
        return(count)


def history_count(count,history_pay):
    print('На вашем счетe - ',count)
    print(history_pay)

def game_count():

    my_count = read_count(FILENAME_FOR_COUNT)
    history = read_history(FILENAME_FOR_HISTORY)

    print(history)

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню ')
        if choice == '1':
            pass
            my_count = add_count(my_count,int(input('Введите сумму на которую хотите пополнить счет :')))
        elif choice == '2':
            pass
            my_count = pay_count(my_count,history)
        elif choice == '3':
            pass
            history_count(my_count,history)
        elif choice == '4':
            write_count(FILENAME_FOR_COUNT,my_count)
            write_history(FILENAME_FOR_HISTORY,history)

            break
        else:
            print('Неверный пункт меню')