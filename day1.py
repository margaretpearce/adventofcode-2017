import sys
digits = [int(x) for x in list(sys.argv[1])]
output = sum([digits[x % len(digits)] if digits[x % len(digits)] == digits[(x + 1) % len(digits)] else 0
          for x in range(0, len(digits))])
print(output)