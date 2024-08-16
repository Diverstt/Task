'''
Условие:
Пусть list[i], list[i+1], list[i+2] – элементы подпоследовательности. В файле
содержится последовательность натуральных чисел. Её элементы могут
принимать целые значения от 1 до 100 000 включительно. Определите
количество троек элементов последовательности, в которых последняя цифра
суммы первого и третьего элемента равняется последней цифре второго
элемента, а сумма кубов цифр предмаксимального и максимального числа
подпоследовательности больше минимального числа этой же
подпоследовательности. Гарантируется, что такой элемент в
последовательности есть. В ответе запишите количество найденных троек,
затем максимальную из сумм элементов таких чисел.
'''

f = open('cache/17_16328.txt')

lst = [int(i) for i in f]


def get(x):
    total = 0
    for i in str(x):
        total += int(i)**3
    return total


cnt = 0
max_cnt = 0
for i in range(len(lst) - 2):
    if (lst[i] + lst[i+2]) % 10 == lst[i+1] % 10:
        cashe = [lst[i], lst[i+1], lst[i+2]]
        max_num = min([lst[i], lst[i+1], lst[i+2]])
        summ = 0
        for i in cashe:
            if i == max_num:
                continue
            else:
                summ += get(i)
        if summ > max_num:
            cnt += 1
            max_cnt = max(max_cnt, sum(cashe))

print(cnt, max_cnt)