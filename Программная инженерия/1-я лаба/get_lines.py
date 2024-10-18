import argparse

def count_lines(file_name):
    try:
        with open(file_name) as file:
            return len(file.readlines())
    except Exception as e:
        return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True)

    args = parser.parse_args()

    print(f'Количество строк в файле: {count_lines(args.file)}')
