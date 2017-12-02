import sys
digits = [int(x) for x in list(sys.argv[1])]

# Puzzle 1
puzzle1_output = sum([digits[x % len(digits)] if digits[x % len(digits)] == digits[(x + 1) % len(digits)] else 0
                      for x in range(0, len(digits))])
print(puzzle1_output)

# Puzzle 2
puzzle2_output = sum([digits[x % len(digits)] if digits[x % len(digits)] == digits[(x + (len(digits) // 2)) % len(digits)]
                      else 0 for x in range(0, len(digits))])
print(puzzle2_output)