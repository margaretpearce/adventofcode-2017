with open("input/day5_1.txt", "r") as input_data:
    offsets = [int(x) for x in input_data.readlines()]

instruction_number = 0
total_steps = 0

while instruction_number < len(offsets):
    instruction_value = offsets[instruction_number]
    offsets[instruction_number] += 1
    instruction_number += instruction_value
    total_steps += 1

print(total_steps)