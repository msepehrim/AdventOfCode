res = []
with open("day09_input.txt") as input_file:
    lines = input_file.readlines()
    for lineI in lines:
        for lineJ in lines:
            x1, y1 = lineI.split(',')
            x2, y2 = lineJ.split(',')
            res.append([(x1, y1), (x2, y2), (abs(int(x1) - int(x2))+ 1) * (abs(int(y1) - int(y2)) + 1)])
maximum = max(res, key = lambda x : x[2])
print(maximum)