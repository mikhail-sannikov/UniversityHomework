import re

with open('../media/5/data.txt') as input_file, open('../media/5/res.txt', 'w') as output_file:
    data = input_file.read()
    regex = r'\(.*\)'

    output_file.write(', '.join(re.findall(regex, data)))
