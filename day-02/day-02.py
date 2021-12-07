import unittest

class TestDay02(unittest.TestCase):

    def test_example_A(self):
        inputFile = open("day-02/example.txt", "r")
        input = inputFile.readlines()
        inputFile.close()

        result = day02A(input)

        print (f'Example result A: {result}')
        self.assertEqual(result, 150)


    def test_puzzleInput_A(self):
        inputFile = open("day-02/input.txt", "r")
        input = inputFile.readlines()
        inputFile.close()

        result = day02A(input)

        print (f'puzzle data result A: {result}')


    def test_example_B(self):
        inputFile = open("day-02/example.txt", "r")
        input = inputFile.readlines()
        inputFile.close()

        result = day02B(input)

        print (f'Example result B: {result}')
        self.assertEqual(result, 900)


    def test_puzzleInput_B(self):
        inputFile = open("day-02/input.txt", "r")
        input = inputFile.readlines()
        inputFile.close()

        result = day02B(input)

        print (f'puzzle data result B: {result}')


def day02A(input):
    horizontalPos = 0
    depth = 0

    for commandString in input:
        commands = commandString.split(" ")
        direction = commands[0]
        count = int(commands[1])

        if direction == "forward":
            horizontalPos += count
        elif direction == "down":
            depth += count
        elif direction == "up":
            depth -= count

    print (f'horizontal position: {horizontalPos} | depth: {depth}')
    return horizontalPos * depth


def day02B(input):
    horizontalPos = 0
    depth = 0
    aim = 0

    for commandString in input:
        commands = commandString.split(" ")
        direction = commands[0]
        count = int(commands[1])

        if direction == "forward":
            horizontalPos += count
            depth += aim * count
        elif direction == "down":
            aim += count
        elif direction == "up":
            aim -= count

    print (f'horizontal position: {horizontalPos} | depth: {depth}')
    return horizontalPos * depth


if __name__ == "__main__":
    unittest.main()
