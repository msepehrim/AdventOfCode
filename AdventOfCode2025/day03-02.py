import os

def argmax(lst, start, end):    
    index = start
    max_value = lst[start]
    if (max_value == 9):
        return start
    for i in range(start + 1, end):
        if lst[i] > max_value:
            max_value = lst[i]
            index = i
            if (max_value == 9):
                return index
    return index
STRING_LENGTH = 12
total_joltage = 0
with open("day03_input.txt") as input_file:
    for line in input_file:
        line = line.strip()
        line_char_list = [*line] 
        line_int_list = list(map(int,line_char_list))
        # max(range(len(line_int_list)), key=line_int_list.__getitem__)
        result = ''
        extracted_digits_count = 0
        max_index = -1
        for i in range(1, STRING_LENGTH + 1):
            max_index = argmax(line_int_list, max_index + 1, len(line_int_list) - (STRING_LENGTH - i))
            result += line[max_index]
        line_joltage = int(result)       
        total_joltage = total_joltage + line_joltage
print(total_joltage)   