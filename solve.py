'''
Для заданного целого числа n считает и возвращает сумму таких повторов: n + nn + nnn + … Число повторов определяется
repeats.
'''


def solve(n, repeats):
    sum_ = 0
    for i in range(1, repeats + 1):
        num = int(str(n) * i)
        sum_ += num
    return sum_


