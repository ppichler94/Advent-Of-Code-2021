from collections import namedtuple

Packet = namedtuple("Packet", ["version", "type"])


def read_input_from_file(file_name):
    input_file = open(file_name, "r")
    input = input_file.readlines()
    input = [x.strip() for x in input]
    input_file.close()
    return input


def parse_packet(data, packets):
    version = int(data[0:3], 2)
    type = int(data[3:6], 2)
    data = data[6:]

    packets.append(Packet(version, type))

    processed = 6
    match type:
        case 4:  # literal
            value = ""
            while True:
                value += data[1:5]
                processed += 5
                if data[0] == "0":
                    data = data[5:]
                    break
                else:
                    data = data[5:]
            value = int(value, 2)

        case _:  # operator
            length_type = data[0]
            if length_type == "0":
                length = int(data[1:16], 2)
                processed += 16
                data = data[16:]
                used = 0
                while used < length:
                    ret = parse_packet(data, packets)
                    data = data[ret:]
                    used += ret
                    processed += ret
            else:
                packet_count = int(data[1:12], 2)
                data = data[12:]
                processed += 12
                for _ in range(packet_count):
                    ret = parse_packet(data, packets)
                    data = data[ret:]
                    processed += ret

    return processed


def run(input):
    lut = {"0": "0000",
           "1": "0001",
           "2": "0010",
           "3": "0011",
           "4": "0100",
           "5": "0101",
           "6": "0110",
           "7": "0111",
           "8": "1000",
           "9": "1001",
           "A": "1010",
           "B": "1011",
           "C": "1100",
           "D": "1101",
           "E": "1110",
           "F": "1111"}
    data = ''.join(lut[x] for x in input[0])
    packets = []

    parse_packet(data, packets)

    return sum(packet.version for packet in packets)


def main():
    example = read_input_from_file("day-16/example.txt")
    input = read_input_from_file("day-16/input.txt")

    examples = [run([x]) for x in example]

    for example in examples:
        print(f"Result example A: {example}\n")

    print(f'Result puzzle data A: {run(input)}\n')
    # print(f'Result example B: {run(example)}\n')
    # print(f'Result puzzle data B: {run(input)}\n')


if __name__ == "__main__":
    main()
