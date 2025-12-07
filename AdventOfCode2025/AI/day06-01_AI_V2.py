from math import prod

list_all = []
list_operator = []

# --- Read file ---
with open("day06_input.txt") as infile:
    for line in infile:
        parts = line.split()

        # Numeric row
        if parts and parts[0].isdigit():
            nums = [int(p) for p in parts if p.isdigit()]
            list_all.append(nums)

        # Operator row
        else:
            ops = [p for p in parts if p in {"+", "*"}]
            list_operator.extend(ops)

# Determine number of columns
col_count = len(list_all[0])

# --- Compute ---
grand_total = 0

for col_idx, op in enumerate(list_operator[:col_count]):
    column = [row[col_idx] for row in list_all]

    if op == "+":
        grand_total += sum(column)
    else:  # "*"
        grand_total += prod(column)

print(grand_total)
