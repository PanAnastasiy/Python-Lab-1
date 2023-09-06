from FuncesOfLabWork_1 import *
from ColorLibrary import *


def message():
    print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED +
          '               ДОБРО ПОЖАЛОВАТЬ В ПРОГРАММУ!              ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')


def menu():
    print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED +
          '          СПИСОК ФУНКЦИЙ, РЕАЛИЗУЕМЫХ В ПРОГРАММЕ :       ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 1.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + ' Задание 1 ( о сумме 1 + 1/2 + 1/3 + ... больше 3 )     ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 2.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + ' Задание 2 ( о всех числах в строке )                   ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 3.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + ' Задание 3 ( о списке из целых чисел )                  ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 4.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + ' Задание 4 ( о словаре и строке I love python )         ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 5.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + ' Задание 5 ( о словаре и ювелирном магазине )           ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 6.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + ' Задание 6 ( о двух множествах )                        ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 7.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + ' Выход из программы.                                    ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' 8.', Style.BRIGHT + Fore.BLUE + '|',
          Style.BRIGHT + Fore.MAGENTA + ' Информация о разработчике.                             ',
          Style.BRIGHT + Fore.BLUE + '|', sep='')
    print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED +
          ' Введите номер подзадачи, которую желаете реализовать :   ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
    return select_function(int(input()))


def select_function(choice):
    match choice:
        case 1:
            task_1()
        case 2:
            task_2()
        case 3:
            task_3()
        case 4:
            task_4()
        case 5:
            task_5()
        case 6:
            task_6()
        case 7:
            print('\n' * 100)
            print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
            print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED +
                  '             Осуществляем выход из программы...           ', Style.BRIGHT + Fore.BLUE + '|')
            print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
            exit(0)
        case 8:
            info_of_developer()
    if choice not in [1, 2, 3, 4, 5, 6, 7, 8]:
        print('\n' * 100)
        print(Style.BRIGHT + Fore.BLUE +
              '+---------------------------------------------------------------------------------+')
        print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED +
              'Введённый вами номер задачи отсутствует в перечне функций. Повторите свой ввод.',
              Style.BRIGHT + Fore.BLUE + '|')
        print(Style.BRIGHT + Fore.BLUE +
              '+---------------------------------------------------------------------------------+')
    return menu()
