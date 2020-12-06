import itertools

with open("input.txt",'r') as expenses:
    values = list(map(int, expenses))

def find_combinations(values, length):
    all_combinations = itertools.combinations(values, length)
    return list(all_combinations)

def question_1():
    for i in find_combinations(values, 2):
        if i[0] + i [1] == 2020:
            return i[0] * i[1]

def question_2():
    for i in find_combinations(values, 3):
        if i[0] + i[1] + i[2] == 2020:
            return i[0] * i[1] * i[2]

print(question_1())
print(question_2())