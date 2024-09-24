from time import perf_counter
from typing import Callable
from random import randrange
from math import log


def main() -> None:
    number = int(''.join([str(randrange(10)) for _ in range(int(input()))]))
    get_number_multipliers(number)


def time_counter(func: Callable) -> Callable:
    def wrapper(number: int) -> list:
        start = perf_counter()
        multipliers = func(number)
        end = perf_counter()

        spent_time = end - start

        with open('results.txt', 'a') as file:
            file.write(
                f'number: {number}, '
                f'{multipliers = }, '
                f'time: {spent_time}, '
                f'ln(m)/n: {log(len(str(number))) / spent_time}\n'
            )

        return multipliers

    return wrapper


@time_counter
def get_number_multipliers(number: int) -> list:
    multipliers = []
    simple_digit = 2

    while simple_digit * simple_digit <= number:
        if number % simple_digit:
            simple_digit += 1
        else:
            number //= simple_digit
            multipliers.append(simple_digit)

    if number > 1:
        multipliers.append(number)

    return multipliers


if __name__ == '__main__':
    main()
