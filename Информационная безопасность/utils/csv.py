import csv

from consts import RESULTS_DIRECTORY


def write_in_file(data: list[list], filename: str = 'data.csv', mode: str = 'w') -> None:
    file_path = RESULTS_DIRECTORY + filename

    with open(file_path, mode, newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
