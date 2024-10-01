from math import log
from random import randrange

from utils.csv import write_in_file
from utils.time import time_counter


def main() -> None:
    start_number_len = int(input('Начальная длина числа: '))
    end_number_len = int(input('Конечная длина числа: '))

    data = [['number', 'multipliers', 'spent_time', 'ln(m)/n']]

    for number_len in range(start_number_len, end_number_len + 1):
        number = int(''.join((str(randrange(10)) for _ in range(number_len))))
        multipliers, spent_time = get_number_multipliers(number)
        progress = log(number_len / spent_time)

        data.append([number, multipliers, spent_time, progress])

    write_in_file(data, 'statistic.csv')


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
