from typing import Any


import re
from itertools import combinations

class Diagram:
    def __init__(self, line) -> None:        
        self.buttons = re.findall(r"\(\d+(?:,\d+)*\)", line)
        self.propagated_buttons = []
        self.joltage = line.split(' ')[-1].strip()
        self.joltages = self.joltage.strip('{}').split(',')
        self.joltages = list(map(int, self.joltages))
        self.var_joltages = [0 for i in range(len(self.joltages))]
        self.propagate()
        
    def press_button(self, index : int):
        button_int = list(map(int, self.buttons[index].strip('()').split(',')))
        for b in button_int:
            self.var_joltages[b] += 1

    def get_min_joltage(self, button : tuple) -> int:
        return min(self.joltages[b] for b in button)

    def propagate(self):        
        for i in range(len(self.buttons)):
            button_tuple = tuple(map(int, self.buttons[i].strip('()').split(',')))
            min_joltaje = self.get_min_joltage(button_tuple)
            for j in range(min_joltaje):
                self.propagated_buttons.append(i)

    def button_pressed_count(self):
        for i in range(1, len(self.propagated_buttons) + 1):
            comb = combinations(self.propagated_buttons, i)
            for cmb in comb:
                self.var_joltages = [0 for i in range(len(self.joltages))]
                for c in cmb:
                    self.press_button(c)
                print(self.var_joltages)
                if self.var_joltages == self.joltages:
                    return i
        return 0

with open("day10_input.txt") as input_file:
    lines = input_file.readlines()

min_list = []
for line in lines:
    diagram = Diagram(line)
    min_list.append(diagram.button_pressed_count())
    print(min_list)
    print(sum(min_list))
print(min_list)
print(sum(min_list))
    