file_pointer = 0
with open("day05_input.txt") as input_file:
    interval_list = []
    for line in input_file:
        file_pointer += 1
        if line == "\n" or line == "" or line is None:
            break
        start, end = line.strip().split("-")
        interval_list.append((start, end))
    id_list = []            
    for line in input_file:
        id_list.append(int(line.strip()))

    found = 0
    for id in id_list:
        for start, end in interval_list:
            if id >= int(start) and id <= int(end):
                found += 1
                break

    print (found)