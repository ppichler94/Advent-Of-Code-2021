def read_input_from_file(file_name):
    input_file = open(file_name, "r")
    input = input_file.readlines()
    input = [x.strip() for x in input]
    input_file.close()
    return input


def day10a(input):
    point_table = {")": 3, "]": 57, "}": 1197, ">": 25137}
    matching_character = {"(": ")", "[": "]", "{": "}", "<": ">"}
    points = 0
    for line in input:
        stack = []
        for character in line:
            if character in ["(", "[", "{", "<"]:
                stack.append(character)
            else:
                last_character = stack.pop()
                required_character = matching_character[last_character]
                if (character != required_character):
                    points += point_table[character]
    return points


def day10b(input):
    return 0


def main():
    example = read_input_from_file("day-10/example.txt")
    input = read_input_from_file("day-10/input.txt")

    print(f'Result example A: {day10a(example)}\n')
    print(f'Result puzzle data A: {day10a(input)}\n')
    print(f'Result example B: {day10b(example)}\n')
    print(f'Result puzzle data B: {day10b(input)}\n')


if __name__ == "__main__":
    main()
