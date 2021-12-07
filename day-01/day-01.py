import unittest

class TestDay01(unittest.TestCase):

    def test_example_A(self):
        inputFile = open("day-01/example.txt", "r")
        input = inputFile.readlines()
        inputFile.close()

        result = day01A(input)

        print (f'Example result A: {result}')
        self.assertEqual(result, 7)


    def test_puzzleInput_A(self):
        inputFile = open("day-01/input.txt", "r")
        input = inputFile.readlines()
        inputFile.close()

        result = day01A(input)

        print (f'puzzle data result A: {result}')


    def test_example_B(self):
        inputFile = open("day-01/example.txt", "r")
        input = inputFile.readlines()
        inputFile.close()

        result = day01B(input)

        print (f'Example result B: {result}')
        self.assertEqual(result, 5)


    def test_puzzleInput_B(self):
        inputFile = open("day-01/input.txt", "r")
        input = inputFile.readlines()
        inputFile.close()

        result = day01B(input)

        print (f'puzzle data result B: {result}')


def day01A(input):
    increase = 0
    previous = int(input.pop(0))
    for current in input:
        value = int(current)
        if (value > previous):
            increase += 1
        previous = value

    return increase


def day01B(input):
    depthOfWindow = []
    for i in range(0, len(input)-2):
        sum = 0
        for j in range(0, 3):
            sum += int(input[i+j])
        depthOfWindow.append(sum)

    increase = 0
    previous = depthOfWindow.pop(0)
    for value in depthOfWindow:
        if (value > previous):
            increase += 1
        previous = value

    return increase


if __name__ == "__main__":
    unittest.main()
