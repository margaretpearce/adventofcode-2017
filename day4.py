valid_passphrases_part_a = 0
valid_passphrases_part_b = 0

with open("input/day4_1.txt", "r") as input_data:
    for line in input_data:
        phrases_list = line.replace('\n', '').split(' ')
        phrases_set = set(phrases_list)
        valid_passphrases_part_a += 1 if len(phrases_list) == len(phrases_set) and len(phrases_list) > 0 else 0

        phrases_list_sorted = [''.join(sorted(x)) for x in phrases_list]
        phrases_set_sorted = set(phrases_list_sorted)
        valid_passphrases_part_b += 1 if len(phrases_list_sorted) == len(phrases_set_sorted) and \
                                         len(phrases_list_sorted) > 0 else 0

print(valid_passphrases_part_a)
print(valid_passphrases_part_b)