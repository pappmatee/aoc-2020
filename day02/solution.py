PASSWORD_LIST = []

def split_lines(lines):
    line = lines.split()
    letter_range = line[0].split('-')
    letter_min = letter_range[0]
    letter_max = letter_range[1]
    key_letter = line[1][0]
    password = line[2]

    new_line = [letter_min, letter_max, key_letter, password]

    PASSWORD_LIST.append(new_line)


with open("input.txt",'r') as input_file:
    for lines in input_file:
        split_lines(lines)


def is_valid(letter, password, letter_min, letter_max):
    letter_count = password.count(letter)
    return letter_count >= int(letter_min) and letter_count <= int(letter_max)


def check_policies():
    valid_policies = 0

    for data in PASSWORD_LIST:
        letter_min = data[0]
        letter_max = data[1]
        key_letter = data[2]
        password = data[3]

        if is_valid(key_letter, password, letter_min, letter_max):
            valid_policies = valid_policies + 1
    
    return valid_policies


result = check_policies()
print(result)