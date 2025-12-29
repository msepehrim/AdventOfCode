from collections import defaultdict

with open("day11_input_test.txt") as input_file:
    lines = input_file.readlines()

graph = defaultdict(set)
for line in lines:
    key = line.split(":")[0].strip()
    values = line.split(":")[1].strip().split(' ')
    for value in values:
        graph[key].add(value.strip())

print(graph)
