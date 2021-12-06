import unittest

class TestDay01(unittest.TestCase):

    def test_example(self):
        input = """ 199
                    200
                    208
                    210
                    200
                    207
                    240
                    269
                    260
                    263 """

        result = day01(input.split("\n"))

        print (f'Example result: {result}')
        self.assertEqual(result, 7)


    def test_puzzleInput(self):
        inputFile = open("day-01/input.txt", "r")
        input = inputFile.readlines()

        result = day01(input)

        print (f'puzzle data result: {result}')


def day01(input):
    increase = 0
    previous = int(input.pop(0))
    for current in input:
        value = int(current)
        if (value > previous):
            increase += 1
        previous = value

    return increase

if __name__ == "__main__":
    unittest.main()
