#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# с использованием многопоточности для заданного значения x найти сумму ряда S с точностью члена ряда по абсолютному
# значению e = 10^-7 и произвести сравнение полученной суммы с контрольным значением функции для двух бесконечных рядов.
import math
import threading


class SumThread(threading.Thread):
    def __init__(self, x, eps):
        threading.Thread.__init__(self)
        self.x = x
        self.eps = eps
        self.sum = 0

    def run(self):
        n = 0
        while True:
            term = (self.x ** n * (math.log(3)) ** n) / math.factorial(n)
            if abs(term) < self.eps:
                break
            self.sum += term
            n += 1


def compare_sums(x, y, eps):
    thread1 = SumThread(x, eps)
    thread2 = SumThread(y, eps)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    sum1 = thread1.sum
    sum2 = thread2.sum

    print(f"Сумма ряда для x: {sum1}")
    print(f"Сумма ряда для y: {sum2}")

    if abs(sum1 - sum2) < eps:
        print("Суммы рядов равны.")
    else:
        print("Суммы рядов не равны.")


compare_sums(1, 3 ** 1, 10 ** -7)

if __name__ == "__main__":
    main()
