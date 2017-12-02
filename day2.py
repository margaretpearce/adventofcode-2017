checksum_1 = 0
checksum_2 = 0

with open("input/day2_1.txt", "r") as input_data:
    for line in input_data:
        digits = [int(x) for x in line.split()]

        # Puzzle 1
        checksum_1 += max(digits) - min(digits)

        # Puzzle 2
        unique_digits = list(set(digits))
        checksum_2 += sum([int(unique_digits[x] / unique_digits[y])
                           if unique_digits[x] % unique_digits[y] == 0 and x != y else 0
                           for x in range(0, len(unique_digits))
                           for y in range(0, len(unique_digits))])

print(checksum_1)
print(checksum_2)
