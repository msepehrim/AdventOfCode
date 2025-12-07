beams = []
splitters = []
hits_count = 0
with open("day07_input.txt") as input_file:
    line = input_file.readline()
    beams = [str(line).index("S")]
    for line in input_file:
        splitters.extend([index for index, ch in enumerate(line) if ch == '^'])
        if (splitters):
            for spl_index in splitters:
                if beams.__contains__(spl_index):
                    hits_count += 1
                    beams.remove(spl_index)
                    if spl_index - 1 >= 0 and not beams.__contains__(spl_index - 1):
                        beams.extend([spl_index - 1])
                    if spl_index + 1 < len(line) - 1 and not beams.__contains__(spl_index + 1):
                        beams.extend([spl_index + 1]) 
            splitters.clear()
print(hits_count)   
        
        