import numpy as np


def readInputFromFile(fileName):
    inputFile = open(fileName, "r")
    input = inputFile.readlines()
    input = [x.strip() for x in input]
    inputFile.close()
    return input


class Population:
    
    def __init__(self, input) -> None:
        self.population = np.array([int(x) for x in input[0].split(",")])

    def __tick(self):
        self.population -= 1

    def __spawnNew(self):
        zeros = self.population == 0
        self.population[zeros] = 7
        self.population = np.append(self.population, [9] * np.count_nonzero(zeros))

    def simulateDays(self, numberOfDays):
        for day in range(0, numberOfDays):
            self.__spawnNew()
            self.__tick()

    def size(self):
        return self.population.size


def day06A(input):
    population = Population(input)
    population.simulateDays(80)
    return population.size()


def day06B(input):
    return 0


def main():
    example = readInputFromFile("example.txt")
    input = readInputFromFile("input.txt")

    print(f'Result example A: {day06A(example)}\n')
    print(f'Result puzzle data A: {day06A(input)}\n')
    print(f'Result example B: {day06B(example)}\n')
    print(f'Result puzzle data B: {day06B(input)}\n')


if __name__ == "__main__":
    main()
