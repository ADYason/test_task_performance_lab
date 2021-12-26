import statistics

FILE = input('Insert a file: ')


def filereader(file):
    file_numbs = []
    with open(file) as f:
        for line in f:
            ''.join(map(str, line))
            line = line.split()
            line = [int(item) for item in line]
            file_numbs.extend(line)
    return file_numbs


def nearest(some_list):
    return min(some_list, key=lambda x: abs(x-statistics.median(some_list)))


def get_answer(some_list, target):
    t = 0
    for num in some_list:
        while num != target:
            if num > target:
                num -= 1
                t += 1
            else:
                num += 1
                t += 1
    return t


print(get_answer(filereader(FILE), nearest(filereader(FILE))))
