
list_all = []

list_operator = []
col_count = 0
with open("day06_input.txt") as input_file :
    for line in input_file:
        list_num = []
        if line.strip()[0].isdigit():
            for num in line.strip().split(" "):
                if num.isdigit():
                    list_num.append(int(num))
            list_all.append(list_num)
            col_count = len(list_num)
        else:
            for op in line.strip().split(" "):
                if op in ("+", "*"):
                    list_operator.append(op)

grand_total = 0
for m in range(col_count):
    if list_operator[m] == '+':
        sub_total = 0
        for l in list_all:
            sub_total = sub_total + l[m]
    else:
        sub_total = 1
        for l in list_all:
            sub_total = sub_total * l[m]
    grand_total = grand_total + sub_total
print(grand_total)



    
    
