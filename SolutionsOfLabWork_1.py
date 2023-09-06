from ColorLibrary import *


def solution_1():
    count, i = 0, 1
    while count < 3:
        count += 1 / i
        i += 1
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '\nОТВЕТ ЗАДАНИЯ 1:',
          Style.BRIGHT + Fore.RED + 'В сумме  1+1/2+1/3+1/4+...+1/n слагаемых должно быть :',
          Style.BRIGHT + Fore.LIGHTCYAN_EX + f' \033[4m{i - 1}\033[0m,',
          Style.BRIGHT + Fore.RED + 'чтобы эта сумма оказалась больше 3, при это сумма будет равна :',
          Style.BRIGHT + Fore.LIGHTCYAN_EX + f' \033[4m{count}\033[0m ')


def solution_2():
    answer = []
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + 'Введите свою строку текста : ')
    st = input()
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + 'Вами была введена строка текста : ', st)
    for i in range(len(st)):
        number = ''
        if st[i].isdigit():
            if st[i] == '0':
                answer.append('0')
                continue
            for g in range(i, len(st)):
                if st[g].isdigit():
                    number += st[g]
                    answer.append(number)
                else:
                    break
    if answer:
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '\nОТВЕТ ЗАДАНИЯ 2:',
              Style.BRIGHT + Fore.RED + f'Все возможные числа, обнаруженные в вашей строке : ', *set(answer))
    else:
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '\nОТВЕТ ЗАДАНИЯ 2:',
              Style.BRIGHT + Fore.RED + f'Увы, но ни одного числа не найдено в заданной вами строке.')


def solution_3():
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX +
          'Введите значения списка через пробел, учтите что все элементы списка есть целые числа :')
    lst_1 = [int(i) for i in input().split()]
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + 'Введите значение переменной С = ')
    C = int(input())
    count = len([i for i in lst_1 if i > C])
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + 'Количество элементов массива, больших С :', count)
    lst_2 = [abs(i) for i in lst_1]
    maxi = max(lst_2)
    if lst_2[-1] == maxi:
        print(Style.BRIGHT + Fore.LIGHTGREEN_EX + 'Максимальный по модулю элемент списка расположен в самом конце, '
              'то есть после него нет никаких элементов.')
    else:
        product = 1
        i = lst_2.index(maxi) + 1
        for g in range(i, len(lst_2)):
            product *= lst_1[g]
        print(Style.BRIGHT + Fore.LIGHTGREEN_EX +
              'Произведение элементов массива, расположенных после максимального по модулю элемента : ', product,
              Style.BRIGHT + Fore.LIGHTGREEN_EX + ', при этом максимальный элемент равен : ', maxi)
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + 'Удаляем положительные элементы списка...')
    lst_1 = [i for i in lst_1 if i <= 0]
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + 'Положительные элементы списка были удалены! '
                                              'Теперь список имеет вид : ', lst_1)


def solution_4():
    dictionary_4 = dict.fromkeys(set('I love Python'), 0)
    for i in 'I love Python':
        dictionary_4[i] += 1
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '\nОТВЕТ ЗАДАНИЯ 4:',
          Style.BRIGHT + Fore.RED + f'Словарь, созданный из исходной строки имеет вид  : ', dictionary_4)


def solution_6():
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + 'Введите элементы первого множества через пробел : ')
    set_1 = set(input().split())
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + "Было инициализировано следующее множество : ", set_1)
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + 'Введите элементы второго множества через пробел : ')
    set_2 = set(input().split())
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + "Было инициализировано следующее множество : ", set_2)
    return set_1.difference(set_2)

# 5.	Реализуйте программу «Ювелирный магазин», которая будет включать в себя шесть пунктов меню.
# У вас есть словарь, где ключ – название изделия. Значение – список, который содержит состав изделия
# (золото, серебро, и т.п.)
# цену и кол-во (шт. ), которое есть в магазине.
# 1.	Просмотр описания: название – описание
# 2.	Просмотр цены: название – цена.
# 3.	Просмотр количества: название – количество.
# 4.	Всю информацию.
# 5.	Покупка
# В пункте «Покупка» необходимо совершить покупку, с клавиатуры вводите название изделия и его кол-во,
# n – выход из программы. Посчитать цену выбранных товаров и сколько товаров осталось в изначальном списке.
# 6 До свидания – 2 балла


dictionary = {
                  'Кольцо': ['Золото', 20, 10000],
                  'Серьги': ['Серебро', 30, 20000],
                  'Цепочка': ['Платина', 10, 5000],
                  'Браслет': ['Палладий', 40, 30000],
                  'Подвеска': ['Иридий', 5, 100000]
             }


def solution_5():
    menu_shop()
    while True:
        if select_function_shop(int(input())) == 0:
            break


def table_header():
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX +
          '+-------------------------------------------------------------------+\n'
          '|                Ювелирный магазин "ПАНовская печать"               |\n'
          '+------------------+--------+--------+---------+---------+----------+\n'
          '| НАЗВАНИЕ ИЗДЕЛИЯ | КОЛЬЦО | СЕРЬГИ | ЦЕПОЧКА | БРАСЛЕТ | ПОДВЕСКА |\n'
          '+------------------+--------+--------+---------+---------+----------+'
          )


def description_1():
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX +
          f'|  СОСТАВ ИЗДЕЛИЯ  |  {dictionary["Кольцо"][0]}| {dictionary["Серьги"][0]}|  {dictionary["Цепочка"][0]}|'
          f' {dictionary["Браслет"][0]}|    {dictionary["Подвеска"][0]}|\n'
          '+------------------+--------+--------+---------+---------+----------+')


def description_2():
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX +
          f'|       ЦЕНА       |   {dictionary["Кольцо"][2]}|   {dictionary["Серьги"][2]}|     '
          f'{dictionary["Цепочка"][2]}|    {dictionary["Браслет"][2]}|    {dictionary["Подвеска"][2]}|\n'
          '+------------------+--------+--------+---------+---------+----------+')


def description_3():
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX +
          f'|    КОЛИЧЕСТВО    |      {dictionary["Кольцо"][1]}|      {dictionary["Серьги"][1]}|       '
          f'{dictionary["Цепочка"][1]}|       {dictionary["Браслет"][1]}|         {dictionary["Подвеска"][1]}|\n'
          '+------------------+--------+--------+---------+---------+----------+')


def description_4():
    description_1()
    description_2()
    description_3()


def shopping():
    keys = ('Кольцо', 'Браслет', 'Серьги', 'Подвеска', 'Цепочка')
    price_of_product = 0
    while True:
        table_header()
        print(Style.BRIGHT + Fore.LIGHTGREEN_EX +
              '|    Какое изделие вы желаете приобрести? Введите его название :    |\n'
              '+-------------------------------------------------------------------+\n')
        name_of_product = input().lower()
        name_of_product = name_of_product[0].upper() + name_of_product[1:]
        if name_of_product not in keys:
            print(Style.BRIGHT + Fore.LIGHTRED_EX +
                  '+-------------------------------------------------------------------+\n'
                  '|    Заданный товар вами товар отсутствует в нашем ассортименте.    |\n'
                  '+-------------------------------------------------------------------+\n')
        else:
            print(Style.BRIGHT + Fore.LIGHTRED_EX +
                  '+-------------------------------------------------------------------+\n'
                  '|          Какое количество изделий вы желаете приобрести?          |\n'
                  '+-------------------------------------------------------------------+')
            count_of_product = int(input())
            if count_of_product < 0:
                print(Style.BRIGHT + Fore.LIGHTGREEN_EX +
                      'Некорректный ввод.')
                continue
            if dictionary[name_of_product][1] < count_of_product:
                print(Style.BRIGHT + Fore.LIGHTGREEN_EX +
                      'Для такой покупки у нас не хватает изделий, которые вы выбрали.')
            else:
                price_of_product += count_of_product*dictionary[name_of_product][2]
                dictionary[name_of_product][1] = dictionary[name_of_product][1] - count_of_product
        print(Style.BRIGHT + Fore.LIGHTRED_EX +
              '+-------------------------------------------------------------------+\n'
              '|          Желаете продолжить покупки? (1|0?)                       |\n'
              '+-------------------------------------------------------------------+\n')
        if int(input()):
            continue
        else:
            break
    print(Style.BRIGHT + Fore.LIGHTBLUE_EX + '+-------------------------------------------------------------------+\n|',
          Style.BRIGHT + Fore.RED +
          '          ЦЕНА ЗА ВСЕ ВЫБРАННЫЕ ВАМИ ИЗДЕЛИЯ РАВНА :     ',
          Style.BRIGHT + Fore.LIGHTCYAN_EX + f' \033[4m{price_of_product}\033[0m ',
          Style.BRIGHT + Fore.LIGHTBLUE_EX + '|',
          Style.BRIGHT + Fore.LIGHTBLUE_EX + '\n+-------------------------------------------------------------------+\n')


def menu_shop():
    print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED +
          '            Ювелирный магазин "ПАНовская печать"          ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 1.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + '  Просмотр описания: название – описание.               ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 2.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + '  Просмотр цены: название – цена.                       ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 3.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + '  Просмотр количества: название – количество.           ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 4.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + '  Вся информация.                                       ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 5.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + '  Покупка.                                              ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 6.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + '  До свидания                                           ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED +
          ' Введите номер подзадачи, которую желаете реализовать :   ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+------------------------------------------------------------+')


def select_function_shop(your_choice):
    match your_choice:
        case 1:
            print('\n' * 100)
            table_header()
            description_1()
        case 2:
            print('\n' * 100)
            table_header()
            description_2()
        case 3:
            print('\n' * 100)
            table_header()
            description_3()
        case 4:
            print('\n' * 100)
            table_header()
            description_4()
        case 5:
            print('\n' * 100)
            shopping()
        case 6:
            print('\n' * 100)
            print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
            print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED +
                  '       Осуществляем выход из ювелирного магазина...       ', Style.BRIGHT + Fore.BLUE + '|')
            print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
            return 0
    if your_choice not in [1, 2, 3, 4, 5, 6]:
        print('\n' * 100)
        print(
            Style.BRIGHT + Fore.BLUE +
            '+---------------------------------------------------------------------------------+')
        print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED +
              'Введённый вами номер задачи отсутствует в перечне функций. Повторите свой ввод.',
              Style.BRIGHT + Fore.BLUE + '|')
        print(
            Style.BRIGHT + Fore.BLUE +
            '+---------------------------------------------------------------------------------+')
    return menu_shop()
