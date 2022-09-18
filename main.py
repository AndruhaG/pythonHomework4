import random

def Zadacha1():
# Пользователь вводит число, Вам необходимо вывести число Пи
# с той точностью знаков после запятой, сколько указал пользователь

    num = int(input('Введите,сколько чисел после запятой будет выводиться: '))
    pi = (1 / 16 ** 0) * (4 / (8 * 0 + 1) - 2 / (8 * 0 + 4) - 1 / (8 * 0 + 5) - 1 / (8 * 0 + 6))

    for k in range(1, num):
        m = (1 / (16 ** k)) * (4 / (8 * k + 1) - 2 / (8 * k + 4) - 1 / (8 * k + 5) - 1 / (8 * k + 6))
        pi += m
    print(round(pi, num))


def Zadacha2():
# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

    m = int(input("Введите число: "))
    i = 2
    lst = []
    number = m
    while i <= m:
        if m % i == 0:
            lst.append(i)
            m //= i
            i = 2
        else:
            i += 1
    print(f'Простые множители числа', number, 'это числа:' ,lst)


def Zadacha3():
# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

    n = int(input('Введите число чисел в массиве: '))
    lst = [int(random.randint(0, 10)) for i in range(n)]
    print(f"Исходный список: {lst}")
    new_lst = []
    [new_lst.append(i) for i in lst if i not in new_lst]
    print(f"Список из неповторяющихся элементов: {new_lst}")



def Zadacha4():
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

    k = int(input("Введите натуральную степень k = "))

    lst = [random.randint(0, 101) for i in range(k + 1)]

    lst = lst[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst) - i - 1}'
                if lst[i + 1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i + 1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    print(wr)


# Zadacha1()
# Zadacha2()
# Zadacha3()
# Zadacha4()



