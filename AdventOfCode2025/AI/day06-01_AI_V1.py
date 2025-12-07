list_all = []
list_operator = []

with open("day06_input.txt") as infile:
    for line in infile:
        parts = line.split()
        # Numeric line
        if parts and parts[0].isdigit():
            nums = [int(p) for p in parts if p.isdigit()]
            list_all.append(nums)
        # Operator line
        else:
            ops = [p for p in parts if p in {"+", "*"}]
            list_operator.extend(ops)

col_count = len(list_all[0])

grand_total = 0

for col_idx, op in enumerate(list_operator[:col_count]):
    column_values = [row[col_idx] for row in list_all]

    if op == "+":
        sub_total = sum(column_values)
    else:  # op == "*"
        sub_total = 1
        for v in column_values:
            sub_total *= v

    grand_total += sub_total

print(grand_total)
