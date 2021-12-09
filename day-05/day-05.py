import numpy as np


def readInputFromFile(fileName):
    inputFile = open(fileName, "r")
    input = inputFile.readlines()
    input = [x.strip() for x in input]
    inputFile.close()
    return input


class Map:
    def __init__(self, input):
        self.parseInput(input)
        self.calculateDimension()
        self.map = np.zeros([self.height, self.width], dtype=int)
        self.addLines()

    def parseInput(self, input):
        self.startCoordinates = np.empty([len(input), 2], dtype=int)
        self.endCoordinates = np.empty([len(input), 2], dtype=int)
        for index, line in enumerate(input):
            coords = line.split(" -> ")
            startCoords = coords[0].split(",")
            endCoords = coords[1].split(",")
            self.startCoordinates[index, 0] = int(startCoords[0])
            self.startCoordinates[index, 1] = int(startCoords[1])
            self.endCoordinates[index, 0] = int(endCoords[0])
            self.endCoordinates[index, 1] = int(endCoords[1])

    def calculateDimension(self):
        self.width = 1 + max(self.startCoordinates[:, 0].max(), self.endCoordinates[:, 0].max())
        self.height = 1 + max(self.startCoordinates[:, 1].max(), self.endCoordinates[:, 1].max())

    def addLines(self):
        for index in range(0, self.startCoordinates.shape[0]):
            start = self.startCoordinates[index]
            end = self.endCoordinates[index]
            if start[1] == end[1]:
                self.addHorizontalLine(start[1], start[0], end[0])
            elif start[0] == end[0]:
                self.addVerticalLine(start[0], start[1], end[1])

    def addHorizontalLine(self, y, x1, x2):
        if x2 < x1:
            x1, x2 = x2, x1
        for x in range(x1, x2 + 1):
            self.map[y, x] += 1

    def addVerticalLine(self, x, y1, y2):
        if y2 < y1:
            y1, y2 = y2, y1
        for y in range(y1, y2 + 1):
            self.map[y, x] += 1

    def getNumberOfOverlaps(self):
        return self.map[self.map > 1].size


def day05A(input):
    map = Map(input)

    return map.getNumberOfOverlaps()


def day05B(input):
    return 0


def main():
    example = readInputFromFile("example.txt")
    input = readInputFromFile("input.txt")

    print(f'Result example A: {day05A(example)}\n')
    print(f'Result puzzle data A: {day05A(input)}\n')
    # print(f'Result example B: {day05B(example)}\n')
    # print(f'Result puzzle data B: {day05B(input)}\n')


if __name__ == "__main__":
    main()
