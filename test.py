"""
1
Разработайте функцию, которая принимает целое число в качестве аргумента и возвращает строку,
содержащую это число и слово "компьютер" в нужном склонении по падежам в зависимости от числа.
Например, при вводе числа 25 функция должна возвращать
"25 компьютеров", для числа 41 — "41 компьютер", а для числа 1048 — "1048 компьютеров".
"""


def computers(n: int):
    if n % 100 in range(11, 20):
        return str(n) + " компьютеров"
    elif n % 10 == 1:
        return str(n) + " компьютер"
    elif n % 10 in range(2, 5):
        return str(n) + " компьютера"
    else:
        return str(n) + " компьютеров"


"""
2
Написать функцию/метод,
которая на вход получает массив положительных целых чисел произвольной длины. 
Например [42, 12, 18]. На выходе возвращает массив чисел,
которые являются общими делителями для всех указанных числе. В примере это будет [2, 3, 6].
"""


def find_common_divisors(numbers):
    max_num = max(numbers)
    divisors = []

    for i in range(1, max_num + 1):
        if all(num % i == 0 for num in numbers):
            divisors.append(i)

    return divisors


numbers = [42, 12, 18]
common_divisors = find_common_divisors(numbers)
print(common_divisors)

"""
3
Написать функцию/метод, которая возвращает массив простых чисел в диапазоне
(2 числа - минимальное и максимальное) заданных чисел.
Например, на вход переданы 2 числа: от 11 до 20
(диапазон считается включая граничные значения).
"""


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def find_primes_in_range(min_num, max_num):
    primes = []
    for num in range(min_num, max_num + 1):
        if is_prime(num):
            primes.append(num)
    return primes


min_num = 11
max_num = 20
prime_numbers = find_primes_in_range(min_num, max_num)
print(prime_numbers)

"""
4
Написать метод, который в консоль выводит таблицу умножения.
На вход метод получает число, до которого выводит таблицу умножения.
В консоли должна появиться таблица. Например, если на вход пришло число 5, то получим:
"""


def multiplication_table(n: int):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i} * {j} = {i * j}")
        print()


multiplication_table("Укажите свое число")
