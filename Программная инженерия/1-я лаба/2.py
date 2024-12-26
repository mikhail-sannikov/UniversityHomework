with open('media/2/data.txt') as input_file, open('media/2/res.txt', 'w') as output_file:
    counter = 0

    for line in input_file.readlines():
        counter += 1
        output_file.write(f'В строке {counter} {len(line.split())} слов(а)\n')

    output_file.write(f'Количество строк: {counter}')
