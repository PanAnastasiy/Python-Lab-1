from SolutionsOfLabWork_1 import *


def task_1():
    print('\n' * 100)
    print(Style.BRIGHT + Fore.BLUE + '+----------------------------------------------------------------------------'
                                     '--------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + 'УСЛОВИЕ ЗАДАНИЯ 1:',
          Style.BRIGHT + Fore.LIGHTMAGENTA_EX +
          ' Сколько слагаемых должно быть  в сумме  1+1/2+1/3+1/4+...+1/n, чтобы эта сумма оказалась больше 3.',
          Style.BRIGHT + Fore.BLUE + '|',)
    print(Style.BRIGHT + Fore.BLUE + '+----------------------------------------------------------------------------'                             
                                     '--------------------------------------------+')
    solution_1()
    print(Style.BRIGHT + Fore.BLUE + '\n\n\n+------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTCYAN_EX +
          '               ЗАДАНИЕ 1 УСПЕШНО ВЫПОЛНЕНО!               ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+------------------------------------------------------------+')


def task_2():
    print('\n' * 100)
    print(Style.BRIGHT + Fore.BLUE + '+---------------------------------------------------------'
                                     '--------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX + 'УСЛОВИЕ ЗАДАНИЯ 2:',
          Style.BRIGHT + Fore.LIGHTMAGENTA_EX +
          ' Ввести строку текста. Вывести на экран все числа, которые встречаются в строке.',
          Style.BRIGHT + Fore.BLUE + '|', )
    print(Style.BRIGHT + Fore.BLUE + '+---------------------------------------------------------'
                                     '--------------------------------------------+')
    solution_2()
    print(Style.BRIGHT + Fore.BLUE + '\n\n\n+------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTCYAN_EX +
          '               ЗАДАНИЕ 2 УСПЕШНО ВЫПОЛНЕНО!               ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+------------------------------------------------------------+')


def task_3():
    print('\n' * 100)
    print(Style.BRIGHT + Fore.BLUE + '+---------------------------------------------------------'
                                     '--------------------------------------------+')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + 'УСЛОВИЕ ЗАДАНИЯ 3:',
          'В списке, состоящем из целых чисел, вычислить:\n'
          '- количество элементов массива, больших С;\n'
          '- произведение элементов массива, расположенных после\n'
          'максимального по модулю элемента.\n'
          '- удалить все положительные элементы списка')
    print(Style.BRIGHT + Fore.BLUE + '+---------------------------------------------------------'
                                     '--------------------------------------------+')
    solution_3()
    print(Style.BRIGHT + Fore.BLUE + '\n\n\n+------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTCYAN_EX +
          '               ЗАДАНИЕ 3 УСПЕШНО ВЫПОЛНЕНО!               ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+------------------------------------------------------------+')


def task_4():
    print('\n' * 100)
    print(Style.BRIGHT + Fore.BLUE + '+---------------------------------------------------------'
                                     '--------------------------------------------+')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' УСЛОВИЕ ЗАДАНИЯ 4:',
          Style.BRIGHT + Fore.LIGHTMAGENTA_EX +
          "Создайте словарь из строки ' I love Python' следующим образом: в\n"
          " качестве ключей возьмите символы строки, а значениями пусть будут\n"
          " числа, соответствующие количеству вхождений данной\n "
          "буквы в строку.")
    print(Style.BRIGHT + Fore.BLUE + '+---------------------------------------------------------'
                                     '--------------------------------------------+')
    solution_4()
    print(Style.BRIGHT + Fore.BLUE + '\n\n\n+------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTCYAN_EX +
          '               ЗАДАНИЕ 4 УСПЕШНО ВЫПОЛНЕНО!               ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+------------------------------------------------------------+')


def task_5():
    print('\n' * 100)
    print(Style.BRIGHT + Fore.BLUE + '+---------------------------------------------'
                                     '--------------------------------------------+')
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + ' УСЛОВИЕ ЗАДАНИЯ 5:',
          Style.BRIGHT + Fore.LIGHTMAGENTA_EX +
          ' Реализуйте программу «Ювелирный магазин», которая будет\n'
          ' включать в себя шесть пунктов меню. У вас есть словарь, где ключ –\n'
          ' название изделия. Значение – список, который содержит состав\n'
          ' изделия(золото, серебро,и т.п.), цену и кол-во (шт),которое есть в\n'
          ' магазине.')
    print(Style.BRIGHT + Fore.BLUE + '+---------------------------------------------'
                                     '--------------------------------------------+')
    solution_5()


def task_6():
    print('\n' * 100)
    print(Style.BRIGHT + Fore.BLUE + '+---------------------------------------------------------------------------'
                                     '--------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTYELLOW_EX +
          'УСЛОВИЕ ЗАДАНИЯ 6:',
          Style.BRIGHT + Fore.LIGHTMAGENTA_EX +
          ' Даны два множества. Вывести на экран элементы первого множества, которых нет во втором множестве.',
          Style.BRIGHT + Fore.BLUE + '|',)
    print(Style.BRIGHT + Fore.BLUE + '+---------------------------------------------------------------------------'
                                     '--------------------------------------------+')
    answer = list(solution_6())
    if len(answer) > 0:
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '\nОТВЕТ ЗАДАНИЯ 6:',
              Style.BRIGHT + Fore.RED + 'Элементы первого множества, которых нет во втором множестве :',
              *answer,
              Style.BRIGHT + Fore.RED + '. Для решения задачи использовался метод',
              Style.BRIGHT + Fore.LIGHTCYAN_EX + ' \033[4mdifference.\033[0m ')
    else:
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + '\nОТВЕТ ЗАДАНИЯ 6:',
              Style.BRIGHT + Fore.RED + ' Первое множество является подмножеством второго множества. '
                                        '\nПервое множество не имеет своих уникальных элементов.',
              *answer,
              Style.BRIGHT + Fore.RED + 'Для решения задачи использовался метод',
              Style.BRIGHT + Fore.LIGHTCYAN_EX + ' \033[4mdifference.\033[0m ')
    print(Style.BRIGHT + Fore.BLUE + '\n\n\n+------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.LIGHTCYAN_EX +
          '               ЗАДАНИЕ 6 УСПЕШНО ВЫПОЛНЕНО!               ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+------------------------------------------------------------+')


def info_of_developer():
    print('\n' * 100)
    print(Style.BRIGHT + Fore.BLUE +
          '+---------------------------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED +
          ' ПРОГРАММА БЫЛА РАЗРАБОТАНА СТУДЕНТОМ 2 КУРСА :',
          Style.BRIGHT + Fore.LIGHTCYAN_EX + ' ПАНФИЛЕНКО СТАНИСЛАВ ИГОРЕВИЧ ',
          Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE +
          '+---------------------------------------------------------------------------------+')
    name_of_work()
    print(Style.BRIGHT + Fore.BLUE +
          '+----------------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED +
          ' АДРЕС ЭЛЕКТРОННОЙ ПОЧТЫ : ',
          Style.BRIGHT + Fore.LIGHTCYAN_EX + ' stasa_stasa_stasa_stasa@mail.ru  ',
          Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE +
          '+----------------------------------------------------------------+')


def name_of_work():
    print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
    print(Style.BRIGHT + Fore.BLUE + '|', Style.BRIGHT + Fore.RED + '             ЛАБОРАТОРНАЯ РАБОТА №1',
          Style.BRIGHT + Fore.LIGHTCYAN_EX + ' ВАРИАНТ 19           ', Style.BRIGHT + Fore.BLUE + '|')
    print(Style.BRIGHT + Fore.BLUE + '+---+--------------------------------------------------------+')
