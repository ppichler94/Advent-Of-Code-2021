import numpy as np
import networkx as nx


def read_input_from_file(file_name):
    input_file = open(file_name, "r")
    input = input_file.readlines()
    input = [x.strip() for x in input]
    input_file.close()
    return input


def visit_allowed_a(node, path):
    if node == node.lower():
        return sum(x == node for x in path) < 1
    return True


def explore_paths(G, current, path, paths):
    if not visit_allowed_a(current, path):
        return
    path.append(current)
    if current == "end":
        paths.append(path)
        return

    for n in G.adj[current]:
        explore_paths(G, n, list(path), paths)


def day12a(input):
    paths = []
    G = nx.Graph()
    G.add_edges_from([tuple(x.split("-")) for x in input])
    explore_paths(G, "start", [], paths)
    return len(paths)


def day12b(input):
    return 0


def main():
    example = read_input_from_file("day-12/example.txt")
    input = read_input_from_file("day-12/input.txt")

    print(f'Result example A: {day12a(example)}\n')
    print(f'Result puzzle data A: {day12a(input)}\n')
    # print(f'Result example B: {day12b(example)}\n')
    # print(f'Result puzzle data B: {day12b(input)}\n')


if __name__ == "__main__":
    main()
