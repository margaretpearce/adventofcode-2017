with open("input/day7_1.txt", "r") as input_data:
    program_data = [line.replace('\n', '') for line in input_data.readlines()]

parent_nodes = [p for p in program_data if '->' in p]
root_node = ""

for i in range(0, len(parent_nodes)):
    program_name = parent_nodes[i].split('(')[0].strip()
    in_other_nodes = [parent_nodes[x]
                      for x in range(0, len(parent_nodes))
                      if i != x and program_name in parent_nodes[x]]
    if len(in_other_nodes) == 0:
        root_node = program_name
        break

print(root_node)
