import sys
digits = [int(x) for x in sys.argv[1:]]

redistribute_index = 0
redistributed_value = 0
cycles = 0
seen_configurations = []

while str(digits) not in seen_configurations:
    seen_configurations.append(str(digits))
    redistributed_value = max(digits)
    redistribute_index = digits.index(redistributed_value)

    digits[redistribute_index] = 0

    while redistributed_value > 0:
        redistribute_index = (redistribute_index + 1) % len(digits)
        digits[redistribute_index] += 1
        redistributed_value -= 1

    cycles += 1

print(cycles)
print(cycles - seen_configurations.index(str(digits)))