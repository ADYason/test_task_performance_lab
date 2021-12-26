import math

FILE1 = input('Insert a file:')
FILE2 = input('Insert a file:')


def filereader1(file):
    file_numbs = []
    with open(file) as f:
        for line in f:
            ''.join(map(str, line))
            line = line.split()
            line = [float(item) for item in line]
            file_numbs.extend(line)
    return file_numbs


def filereader2(file):
    file_numbs = {}
    with open(file) as f:
        for line in f:
            ''.join(map(str, line))
            line = line.split()
            line = [float(item) for item in line]
            file_numbs[line[0]] = line[1]
    return file_numbs


def get_answer(input1, input2):
    x_point, y_point, r_circle = input1
    new_points = {}
    for x, y in input2.items():
        x = x - x_point
        y = y - y_point
        new_points[x] = y
    for x, y in new_points.items():
        hypotenuse = math.sqrt(x ** 2 + y ** 2)
        if hypotenuse < r_circle:
            print(1)
        elif hypotenuse == r_circle:
            print(0)
        else:
            print(2)


get_answer(filereader1(FILE1), filereader2(FILE2))
