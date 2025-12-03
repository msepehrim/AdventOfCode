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

total_joltage = 0
with open("day03_input.txt") as input_file:
    for line in input_file:
        line = line.strip()
        line_char_list = [*line] 
        line_int_list = list(map(int,line_char_list))
        # max(range(len(line_int_list)), key=line_int_list.__getitem__)
        max_index_1 = argmax(line_int_list, 0, len(line_int_list) - 1)
        max_index_2 = argmax(line_int_list, max_index_1 + 1, len(line_int_list))
        line_joltage = 10 * line_int_list[max_index_1] + line_int_list[max_index_2]
        total_joltage = total_joltage + line_joltage
print(total_joltage)   