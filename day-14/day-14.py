

def read_input_from_file(file_name):
    input_file = open(file_name, "r")
    input = input_file.readlines()
    input = [x.strip() for x in input]
    input_file.close()
    return input


def parse_input(input):
    template = input[0]
    rules = {}
    for line in input[2:]:
        s = line.split(" -> ")
        rules[s[0]] = s[1]
    return [template, rules]


def run_steps(template, rules, step_count):
    for _ in range(10):
        new_template = ""
        pairs = [template[i:i+2] for i in range(len(template) - 1)]
        for pair in pairs:
            new_template += pair[0] + rules[pair]
        new_template += template[-1]
        template = new_template
    return template


def run(input, steps):
    [template, rules] = parse_input(input)
    template = run_steps(template, rules, steps)
    counts = [template.count(x) for x in set(template)]
    return max(counts) - min(counts)


def main():
    example = read_input_from_file("day-14/example.txt")
    input = read_input_from_file("day-14/input.txt")

    print(f'Result example A: {run(example, 10)}\n')
    print(f'Result puzzle data A: {run(input, 10)}\n')
    # print(f'Result example B: {run(example)}\n')
    # print(f'Result puzzle data B: {run(input)}\n')


if __name__ == "__main__":
    main()
