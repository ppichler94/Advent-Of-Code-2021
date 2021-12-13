def readInputFromFile(fileName):
    inputFile = open(fileName, "r")
    input = inputFile.readlines()
    input = [x.strip() for x in input]
    inputFile.close()
    return input


def day08A(input):
    uniqueNumbers = 0
    for line in input:
        outputValue = line.split("|")[1]
        for value in outputValue.split(" "):
            if len(value) in [2, 3, 4, 7]:
                uniqueNumbers += 1
    return uniqueNumbers


def formatInput(input):
    return list(map(lambda w: ''.join(sorted(w)), input))


def findUniques(line, tmp):
    lengthMap = {2: 1, 3: 7, 4: 4, 7: 8}
    for word in line:
        if len(word) in lengthMap:
            tmp[lengthMap[len(word)]] = word


# one character is different between 1 and 6
def find6(line, tmp):
    for word in line:
        if len(word) == 6 and any(character not in word for character in tmp[1]):
            tmp[6] = word
            break


# one character is different between 0 and 4. Also one character difference to 6 (so find 6 first)
def find0(line, tmp):
    for word in line:
        if (len(word) == 6
                and any(character not in word for character in tmp[4])
                and word not in tmp.values()):
            tmp[0] = word
            break


# only 6 character number left after finding 0 and 6
def find9(line, tmp):
    for word in line:
        if len(word) == 6 and word not in tmp.values():
            tmp[9] = word
            break


# all characters of 5 are in 6
def find5(line, tmp):
    for word in line:
        if len(word) == 5 and all(character in tmp[6] for character in word):
            tmp[5] = word
            break


# all characters of 3 are in 9 and 5 (find 5 first)
def find3(line, tmp):
    for word in line:
        if (len(word) == 5
                and all(character in tmp[9] for character in word)
                and word not in tmp.values()):
            tmp[3] = word
            break


# only 5 character number left after finding 5 and 3
def find2(line, tmp):
    for word in line:
        if len(word) == 5 and word not in tmp.values():
            tmp[2] = word
            break


def day08B(input):
    pattern = list(map(formatInput, [line.split("|")[0].strip().split() for line in input]))
    output = list(map(formatInput, [line.split("|")[1].strip().split() for line in input]))
    total = 0

    for line, outputValue in zip(pattern, output):
        tmp = {}

        findUniques(line, tmp)
        find6(line, tmp)
        find0(line, tmp)
        find9(line, tmp)
        find5(line, tmp)
        find3(line, tmp)
        find2(line, tmp)

        code = {v: k for k, v in tmp.items()}

        total += int(''.join(map(str, [code[word] for word in outputValue])))

    return total


def main():
    example = readInputFromFile("day-08/example.txt")
    input = readInputFromFile("day-08/input.txt")

    print(f'Result example A: {day08A(example)}\n')
    print(f'Result puzzle data A: {day08A(input)}\n')
    print(f'Result example B: {day08B(example)}\n')
    print(f'Result puzzle data B: {day08B(input)}\n')


if __name__ == "__main__":
    main()
