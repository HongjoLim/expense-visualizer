import csv
import functools
import re

def main():
    FILE_NAME = 'expenditure.csv'
    lines = read_file(FILE_NAME)
    lines = strip_non_numeric_chars(lines)
    lines = convert_to_abs(lines)
    total_expenditure = add_all_entries(lines)
    print('{:.2f}'.format(total_expenditure))

def read_file(file_name):
    with open(file_name) as f:
        reader = csv.reader(f, delimiter = ',')
        return [row for row in reader]

def strip_non_numeric_chars(entries):
    return [re.sub('[^0-9\-.]', '', str(entry)) for entry in entries]

def convert_to_abs(entries):
    return [abs(float(entry)) for entry in entries]

def add_all_entries(entries):
    return functools.reduce(lambda x, y : x + y, entries)

if __name__ == '__main__':
    main()