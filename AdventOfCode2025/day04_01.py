# import os
# print(os.getcwd())

# def get_node_weight(column, prev, curr, next):
#     weight = 0
#     calc = lambda x : 1 if x == '@' else 0
#     if (prev != ''):
#         weight = calc(prev[column - 1] if column > 0 else 0) + calc(prev[column]) + calc(prev[column + 1] if column < len(prev) - 1 else 0)
#     if (curr != ''):
#         weight = weight + calc(curr[column - 1] if column > 0 else 0) + calc(curr[column]) + calc(curr[column + 1] if column < len(curr) - 1 else 0)
#     if (next != ''):
#         weight = weight + calc(next[column - 1] if column > 0 else 0) + calc(next[column]) + calc(next[column + 1] if column < len(next) - 1 else 0)
#     return weight
    
def get_node_weight(column, prev, curr, next):
    def row_sum(row):
        if not row:
            return 0
        start = max(0, column - 1)
        end = min(len(row) - 1, column + 1)
        return sum(1 for ch in row[start:end + 1] if ch == '@')
    
    return row_sum(prev) + row_sum(curr) + (-1 if curr[i] == '@' else 0) + row_sum(next)

MIN_WEIGHT = 3
total = 0
line_next = None
line_prev = ''
line_curr = ''
with open("day04_input.txt") as input_file:
    while line_next != '':
        if line_curr != '':
            line_prev = line_curr
        if line_next != '' and line_next != None:
            line_curr = line_next
        else:
            line_curr = input_file.readline().strip()
        line_next = input_file.readline().strip()
        for i in range(len(line_curr)):
            if line_curr[i] == '@':
                weight = get_node_weight(i, line_prev, line_curr, line_next)
                if weight <= MIN_WEIGHT:
                    total = total + 1
print(total)

    
    
    
