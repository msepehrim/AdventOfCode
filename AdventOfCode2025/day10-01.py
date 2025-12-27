from typing import Any


import re
from itertools import combinations

class Diagram:
    def __init__(self, line) -> None:
        self.joltage = self.Joltage(line)
        self.light = self.Light(line)
        self.button = self.Button(line, self.light.length())
    
    def get_min(self):
        return self.button.get_min(self.light.light_number)

    class Light:
        def __init__(self, line):
            self.light = line.split(' ')[0]
            self.set()
        def set(self):
            light = self.light.replace(".", "0").replace("#", "1").strip("[]")
            self.light_number = int(light, 2)
        def length(self):
            return len(self.light.strip("[]"))

    class Button:
        def __init__(self, line, length) -> None:
            self.length = length
            self.button = re.findall(r"\(\d+(?:,\d+)*\)", line)
            self.set()
        def set(self):
            self.button_number = []
            for button in self.button:
                button_number = 0
                for number in button.strip('()').split(','):
                    d = 2 ** (self.length - 1 - int(number))
                    button_number += d
                self.button_number.append(button_number)
        def get_min(self, goal):
            for i in range(1, len(self.button_number)):
                comb = combinations(self.button_number, i)
                res = 0
                for c in comb:
                    res = res ^ int(c)
                if res == goal:
                    return i
            return None



    class Joltage:
        def __init__(self, line) -> None:
            self.joltage = line.split(' ')[-1].strip()
    
    # def set(self):
    #     self.set_lights()

    # def set_lights(self):
    #     self.light.set()

with open("day10_input_test.txt") as input_file:
    lines = input_file.readlines()

min_list = []
for line in lines:
    diagram = Diagram(line)
    min_list.append(diagram.get_min())
print(min_list)
    