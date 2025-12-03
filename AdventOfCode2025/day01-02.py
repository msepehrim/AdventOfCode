import os
pointer = 50
password = 0
if os.path.exists("out-01-02.output"):
    os.remove("out-01-02.output")
with open("out-01-02.output", "a") as out_file:
    with open("day01_input.txt") as f:
        for line in f:
            #out_file.write(line[0:-1] + " >>> " + line[1:])
            direction = line[0]
            # out_file.write(line[0:-1] + " >>> " + direction + "+" + line[1:])
            rotation = int(line[1:-1])
            hit_with_rotation = int(rotation / 100)
            if direction == 'L':
                if pointer != 0 and pointer - (rotation % 100) < 0:           
                    password  = password + 1

                pointer = pointer - rotation                
                if pointer < 0:
                    pointer = (-1 * (abs(pointer) % 100)) + 100
            else:
                if pointer + (rotation % 100) > 100:           
                    password  = password + 1
                pointer = (pointer + rotation) % 100 
                
            
            if pointer == 100:
                pointer = 0
            
            if pointer == 0 :
                password = password + 1
            password = password + hit_with_rotation
            out_file.write(line[0:-1] + " pointer " + str(pointer) + " hit " + str(hit_with_rotation) + " pass " + str(password) + os.linesep)
print(password)

