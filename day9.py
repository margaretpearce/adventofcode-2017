"""
Idea:
- Use a stack to store { and }
- If {, add to stack (if not in garbage)
- If }, add current size of stack and then pop from stack (if not in garbage)
- If <, in garbage
- If !, skip next character no matter what it is
- If >, exiting garbage
"""

def count_groups(input):
    groups = []
    group_count = 0
    num_nested_groups = 0

    garbage_group = False
    num_garbage_characters = 0

    i = 0

    while i < len(input):
        char = input[i]

        if garbage_group:
            if char == "!":
                i += 1  # Skip the next character
            elif char == ">":
                garbage_group = False
            else:
                num_garbage_characters += 1
        else:
            if char == "{":
                num_nested_groups += 1
                groups.append(num_nested_groups)
            elif char == "}":
                num_nested_groups -= 1
                group_count += groups.pop()
            elif char == "<":
                garbage_group = True
        i += 1
    return group_count, num_garbage_characters


def main():
    with open('input/day9_1.txt') as input:
        data = input.readline()
        print(count_groups(data))

if __name__ == "__main__":
    main()
