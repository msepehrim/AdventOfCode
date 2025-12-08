def count_hits(filename: str = "day07_input.txt") -> int:
    hits_count = 0

    with open(filename) as input_file:
        # First line: find starting beam position
        first_line = input_file.readline()
        beams = {first_line.index("S")}  # use a set for fast membership

        # Process the rest of the lines
        for line in input_file:
            # Indices of all '^' characters in this line
            splitters = {index for index, ch in enumerate(line) if ch == "^"}

            for spl_index in splitters:
                if spl_index in beams:
                    hits_count += 1
                    beams.remove(spl_index)

                    left = spl_index - 1
                    right = spl_index + 1

                    if left >= 0:
                        beams.add(left)
                    # line often ends with '\n', so use len(line) - 1 as in the original
                    if right < len(line) - 1:
                        beams.add(right)

    return hits_count


if __name__ == "__main__":
    print(count_hits())
