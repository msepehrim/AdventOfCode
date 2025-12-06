file_pointer = 0
with open("day05_input.txt") as input_file:
    interval_list = []
    for line in input_file:
        file_pointer += 1
        if line == "\n" or line == "" or line is None:
            break
        start, end = line.strip().split("-")
        interval_list.append((int(start), int(end)))

    counr = 0
    interval_list.sort(key = lambda x : x[0])
    intrval_prev = None
    for interval in interval_list:
        if intrval_prev is None:
            count = count + interval[1] - interval[0] + 1
        else:
            if interval[0] >



    # id_list = []            
    # for line in input_file:
    #     id_list.append(int(line.strip()))

    # list_all_id = []
    # for start, end in interval_list:
    #     for id in range(int(start), int(end)+1):
    #         if (list_all_id.count(id) == 0):
    #             list_all_id.append(id)
    # print (len(list_all_id))