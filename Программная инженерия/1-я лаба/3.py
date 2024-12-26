with open('media/3/data.txt') as input_file, open('media/3/res.txt', 'w') as output_file:
    for line in input_file.readlines():
        output_file.write(' '.join(line.split()) + '\n')
