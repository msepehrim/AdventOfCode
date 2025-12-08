
def calculate(num):
    total = 0 if num[len(num) - 1][0] == '+' else 1
    for digit_index in range(len(num[0]) - 1):
        sub_number = ''
        for row_index in range(len(num) - 1):
            sub_number += num[row_index][digit_index]
        if num[len(num) - 1][0] == '+':
            total += int(sub_number.strip())
        else:
            total *= int(sub_number.strip())

    return total



grand_total = 0
lines = ''
numbers = ['', '', '', '', '']
with open("day06_input.txt") as input_file :
    lines = input_file.readlines()
for column in range(len(lines[0]) - 1):
    is_all_chars_space = True
    for line_index in range(len(lines)):
        is_all_chars_space = is_all_chars_space and lines[line_index][column] == ' '
        numbers[line_index] += lines[line_index][column]
    if is_all_chars_space  or column == len(lines[0]) - 2:
        if column == len(lines[0]) - 2:
            for i in range(len(numbers) - 1):
                numbers[i] += ' '
        grand_total += calculate(numbers)
        numbers = ['', '', '', '', '']
print(grand_total)

        


    
    
