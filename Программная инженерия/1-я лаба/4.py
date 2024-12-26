import csv

author = input()

with open('media/4/data.csv') as input_file, open('media/4/res.txt', 'w') as output_file:
    reader = csv.reader(input_file)

    for row in list(reader)[1:]:
        if row[0] == author and int(row[2]) < 2019:
            output_file.write(row[1])
