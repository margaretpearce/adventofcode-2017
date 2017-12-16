from collections import Counter


def solve_part_a(program_data):
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
    return root_node


def solve_part_b(program_data, root_node):
    parent_nodes = [p for p in program_data if '->' in p]
    nodes = {}

    # Set weights
    for l in program_data:
        node_name = l.split('(')[0].strip()
        node_weight = int(l.split('(')[1].split(')')[0].strip())
        nodes[node_name] = {"weight": node_weight}

    # Build graph structure
    for p in parent_nodes:
        node_name = p.split('(')[0].strip()
        node_children = p.split('-> ')[1].split(', ')
        nodes[node_name]["children"] = node_children

    # Find imbalance given graph structure
    weight_needed = find_unbalanced_tower_weight(nodes, root_node)
    print(weight_needed)


def find_unbalanced_tower_weight(nodes, root_name):
    for n in nodes:
        nodes[n]["tower_weight"] = get_tower_weight(nodes, n)

    for n in nodes:
        nodes[n]["child_weights"] = get_child_weights(nodes, n)

    # Starting from the root, traverse through the tree until finding the deepest imbalance (BFS)
    nodes_to_check = [root_name]
    unbalanced_node = None

    while nodes_to_check:
        n = nodes_to_check.pop()
        if len(set(nodes[n]["child_weights"])) > 1:
            unbalanced_node = n

            # There is an imbalance somewhere on this branch - keep searching
            for c in nodes[n]["children"]:
                nodes_to_check.insert(0, c)
        # If the child weights match or if there are no child weights, do nothing (balanced)

    # All but one weight should match
    unbalanced_weights = nodes[unbalanced_node]["child_weights"]

    most_common, _ = Counter(unbalanced_weights).most_common(1)[0]
    least_common = set(unbalanced_weights).difference({most_common}).pop()
    difference = most_common - least_common

    # Find the node with the mismatched weight
    node_to_adjust = [n for n in nodes[unbalanced_node]["children"] if nodes[n]["tower_weight"] == least_common].pop()

    # The "correct" weight should be: weight + difference
    correct_weight = nodes[node_to_adjust]["weight"] + difference
    return correct_weight


def get_tower_weight(nodes, root_name):
    return nodes[root_name].get("weight") + \
           sum([get_tower_weight(nodes, c) for c in nodes[root_name].get("children", [])])


def get_child_weights(nodes, root_name):
    return [nodes[c]["tower_weight"] for c in nodes[root_name].get("children", [])]


def main():
    with open("input/day7_1.txt", "r") as input_data:
        program_data = [line.replace('\n', '') for line in input_data.readlines()]

    root_node = solve_part_a(program_data)
    solve_part_b(program_data, root_node)

if __name__ == "__main__":
    main()
