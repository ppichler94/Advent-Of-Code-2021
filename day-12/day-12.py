import numpy as np
import networkx as nx


def read_input_from_file(file_name):
    input_file = open(file_name, "r")
    input = input_file.readlines()
    input = [x.strip() for x in input]
    input_file.close()
    return input


def visit_allowed_a(node, visited_small_caves):
    if node == node.lower():
        return sum(x == node for x in visited_small_caves) < 1
    return True


def visit_allowed_b(node, visited_small_caves):
    if node != "end" and node == node.lower():
        sums = {x: visited_small_caves.count(x) for x in visited_small_caves}
        if node == "start" and sum(x == "start" for x in visited_small_caves) > 0:
            return False
        if sum(v == 2 for v in sums.values()) == 1:
            if node in sums:
                return sums[node] < 1
            else:
                return True
        if sum(v == 2 for v in sums.values()) == 0:
            return True
    return True


def explore_paths(g, current, path, paths, visited_small_caves, visit_allowed):
    if not visit_allowed(current, visited_small_caves):
        return
    if current == current.lower():
        visited_small_caves.append(current)
    path.append(current)
    if current == "end":
        paths[0] += 1
        return

    for n in g.adj[current]:
        explore_paths(g, n, list(path), paths, list(visited_small_caves), visit_allowed)


def day12a(input):
    paths = [0]
    g = nx.Graph()
    g.add_edges_from([tuple(x.split("-")) for x in input])
    explore_paths(g, "start", [], paths, [], visit_allowed_a)
    return paths[0]


def day12b(input):
    paths = [0]
    g = nx.Graph()
    g.add_edges_from([tuple(x.split("-")) for x in input])
    explore_paths(g, "start", [], paths, [], visit_allowed_b)
    return paths[0]


def main():
    example = read_input_from_file("day-12/example.txt")
    input = read_input_from_file("day-12/input.txt")

    print(f'Result example A: {day12a(example)}\n')
    print(f'Result puzzle data A: {day12a(input)}\n')
    print(f'Result example B: {day12b(example)}\n')
    print(f'Result puzzle data B: {day12b(input)}\n')


if __name__ == "__main__":
    main()
