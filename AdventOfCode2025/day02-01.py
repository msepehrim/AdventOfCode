import os
with open("out_day02_01.txt", "a") as day02_out_01:
    with open("day02.txt") as day02_input:
        password = 0
        id_ranges = day02_input.read().split(',')
        # print(id_ranges)
        for id_range in id_ranges:
            start_id = id_range.split('-')[0]
            end_id = id_range.split('-')[1]
            for id in range(int(start_id), int(end_id) + 1):
                if len(str(id)) % 2 == 0:
                    s = (len(str(id)) // 2) 
                    e = len(str(id)) // 2
                    part1 = str(id)[:s]
                    part2 = str(id)[e:]
                    day02_out_01.write(id_range + " >> " + str(id) + " >> " + part1 + " >> " + part2 + os.linesep)
                    if (part1 == part2):
                        password = password + id
        print(password)
38310256125