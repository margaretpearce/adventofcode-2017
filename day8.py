import operator


def part_a(instructions):
    registers = {}

    for i in instructions:
        reg, action, val, _, comp_reg, op, comp_val = i.split(" ")
        val = int(val)
        comp_val = int(comp_val)

        if check_condition(registers.get(comp_reg, 0), op, comp_val):
            multiplier = 1 if action == "inc" else -1
            registers[reg] = registers.get(reg, 0) + (multiplier * val)

    sorted_registers = sorted(registers.items(), key=operator.itemgetter(1))
    return sorted_registers[-1]


def check_condition(comp_reg_val, op, comp_val):
    if op == ">":
        return comp_reg_val > comp_val
    elif op == "<":
        return comp_reg_val < comp_val
    elif op == ">=":
        return comp_reg_val >= comp_val
    elif op == "<=":
        return comp_reg_val <= comp_val
    elif op == "==":
        return comp_reg_val == comp_val
    elif op == "!=":
        return comp_reg_val != comp_val
    else:
        raise NotImplementedError("Operator not implemented")


def main():
    with open("input/day8_1.txt", "r") as input_data:
        instructions = [line.replace('\n', '') for line in input_data.readlines()]
    print(part_a(instructions))


if __name__ == "__main__":
    main()
