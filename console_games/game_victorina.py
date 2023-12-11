import random
def separate(list_fam_per,quantity,count_person):
    result = random.sample(range(0,count_person-1), quantity)
    list_persons = {list_fam_per[i] for i in result}
    return(list_persons)

def victorina():
    birthday_famous_persons = {'Пушкин А.С.':'6.06.1799','Толстой Л.Н.':'9.09.1828','Гоголь н.В':'1.04.1809','Лермонтов М.Ю.':'15.10.1814','Тютчев Ф.И.':'5.12.1803',
                     'Грибоедов А.С.':'15.01.1795','Чехов А.П.':'29.01.1860','Пришвин М.М.':'4.02.1873','Барто А.Л.':'4.02.1906','Крылов И.А.':'13.02.1769' }

   ###  list_famous_persons = ('Пушкин А.С.','Толстой Л.Н.','Гоголь н.В','Лермонтов М.Ю.','Тютчев Ф.И.','Грибоедов А.С.','Чехов А.П.','Пришвин М.М.','Барто А.Л.','Крылов И.А.')
    list_mounth = ('января',"февраля","марта","апреля","мая","июня","июля","августа","сентября","октября","ноября","декабря")
    quantity_question = 5
    ### numbers = [0,1,2,3,4,5,6,7,8,9]
    list_famous_persons = list(birthday_famous_persons.keys())
    print(len(birthday_famous_persons))
    while True:
        answer = 0
        list_choose_persons = separate(list_famous_persons,quantity_question ,len(birthday_famous_persons))
        print(list_choose_persons)
        for i in list_choose_persons:
            print("Введите дату рождения в формате  dd.mm.yyyy  для :  ",i,"    ",end='')
            age = input()
            if age == birthday_famous_persons.get(i):
                answer += 1
            else:
                stroka_bithday = birthday_famous_persons.get(i).split('.')
                print('Правильный ответ - ', stroka_bithday[0],list_mounth[int(stroka_bithday[1])-1], stroka_bithday[2])

        print("Количество правильных ответов : ", answer)
        print("Количество ошибок : ", quantity_question - answer)
        print("Процент правильных ответов : ", answer*100/quantity_question)
        print("Процент ошибок : ", (quantity_question-answer)*100/quantity_question)
        if input('Хотите начать сначала : ') != 'да':
          break
    print('Конец игры')
