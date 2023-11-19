def add_count(count):
    count += int(input('Введите сумму на которую хотите пополнить счет :'))
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
    print('На вашем счете - ',count)
    print(history_pay)

def game_count():
    my_count = 0
    history = []
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню ')
        if choice == '1':
            pass
            my_count = add_count(my_count)
        elif choice == '2':
            pass
            my_count = pay_count(my_count,history)
        elif choice == '3':
            pass
            history_count(my_count,history)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')