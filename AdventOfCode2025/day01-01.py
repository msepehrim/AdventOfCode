import os
pointer = 50
password = 0
with open("out.txt", "a") as out_file:
    with open("day01_input_test.txt") as f:
        for line in f:
            #out_file.write(line[0:-1] + " >>> " + line[1:])
            direction = line[0]
            # out_file.write(line[0:-1] + " >>> " + direction + "+" + line[1:])
            rotation = int(line[1:-1])
            if direction == 'L':
                pointer = pointer - rotation                
                if pointer < 0:
                    pointer = (-1 * (abs(pointer) % 100)) + 100
            else:
                pointer = (pointer + rotation) % 100            
            
            if pointer == 100:
                pointer = 0
            
            if pointer == 0 :
                password = password + 1

            out_file.write(line[0:-1] + " >>> " + str(pointer) + os.linesep)
print(password)

