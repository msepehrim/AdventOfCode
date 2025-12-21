class Diagram:
    class Light:
        def __init__(self, light):
            self.light = light
            self.convert()
        def convert(self):
            light = self.light.replace(".", "0").replace("#", "1")
            self.light_number = int(light, 2)

    class Button:
        pass
    class Joltage:
        pass


with open("day10_input_test.txt") as input_file:
    lines = input_file.readlines()
diagram = Diagram()
for line in lines:
    light = Diagram.Light(line.strip(' ')[0])
    