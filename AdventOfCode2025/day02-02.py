import os
if os.path.exists("out_day02_02.txt"):
    os.remove("out_day02_02.txt")
with open("out_day02_02.txt", "a") as day02_out_02:
    with open("day02.txt") as day02_input:
        password = 0
        id_ranges = day02_input.read().split(',')
        # print(id_ranges)
        for id_range in id_ranges:
            start_id = id_range.split('-')[0]
            end_id = id_range.split('-')[1]
            # is_passed = False
            for id in range(int(start_id), int(end_id) + 1):
                length_of_id = len(str(id))
                for d in range(1, length_of_id // 2 + 1):
                    if len(str(id)) % d == 0:
                        part_count = length_of_id // d
                        parts = [str(id)[i*d:(i+1)*d] for i in range(part_count)]               
                        day02_out_02.write(id_range + " >> " + str(id) + " >> " + str(parts) + os.linesep)
                        all_equal = all(part == parts[0] for part in parts)
                        if all_equal:
                            password = password + id
                            break

        print(password)
                
                
