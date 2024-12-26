n = int(input('n: '))

with open('media/1/input.txt') as input_file, open('media/1/output.txt', 'w') as output_file:
    for line in input_file.readlines():
        if n > len(line):
            output_file.write(line)
