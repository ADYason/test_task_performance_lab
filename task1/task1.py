FILE = input('Insert a file:')

with open(FILE) as f:
    for line in f:
        ''.join(map(str, line))
        line = line.split()

NEW_NUMB = int(line[0])
NEW_LIST = list(range(1, NEW_NUMB+1))
STEP = int(line[1])


def get_answer(some_list, step):
    t = 0
    check_list = []
    answer_list = []
    new_some_list = some_list
    step_count = list(range(step))
    for count in step_count:
        check_list.append(new_some_list[count])
    answer_list.append(check_list[0])
    while some_list[0] is not check_list[-1]:
        t += 1
        check_list.clear()
        step_count = list(range(step*t - t, step*(t+1)-t))
        try:
            for count in step_count:
                check_list.append(new_some_list[count])
        except IndexError:
            new_some_list.extend(some_list)
        for count in step_count:
            check_list.append(new_some_list[count])
        answer_list.append(check_list[0])
    answer_list = int(''.join(map(str, answer_list)))
    print(answer_list)


get_answer(NEW_LIST, STEP)
