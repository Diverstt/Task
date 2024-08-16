'''
Условие:
В файле содержится последовательность натуральных чисел. Элементы
последовательности могут принимать целые значения от 1 до 100 000
включительно. Определите количество пар последовательности, в которых
наибольший общий делитель двух чисел больше суммы цифр максимального
элемента пары. В ответе запишите количество найденных пар, затем
максимальную из сумм элементов таких пар. В данной задаче под парой
подразумевается два идущих подряд элемента последовательности.
'''

f = open('cache/17_16328.txt')

lst = [int(i) for i in f]


def dividers(x):
    lst = []
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            lst.append(i)
            lst.append(x//i)
    return sorted(set(lst))


cnt = 0
max_cnt = 0
for i in range(len(lst) - 1):
    num = max([lst[i], lst[i + 1]])
    sum_num = sum([int(i) for i in str(num)])
    lst1, lst2 = dividers(lst[i]), dividers(lst[i+1])
    lst3 = list(set(lst1) & set(lst2))
    if sum_num < max(lst3):
        cnt += 1
        max_cnt = max(max_cnt, lst[i] + lst[i+1])
print(cnt, max_cnt)