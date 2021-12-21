from collections import namedtuple

Packet = namedtuple("Packet", ["version", "type", "length", "value", "subpackets"])


def read_input_from_file(file_name):
    input_file = open(file_name, "r")
    input = input_file.readlines()
    input = [x.strip() for x in input]
    input_file.close()
    return input


def parse_packet(data):
    version = int(data[0:3], 2)
    type = int(data[3:6], 2)
    data = data[6:]

    value = 0
    length = 6
    subpackets = []
    match type:
        case 4:  # literal
            value = ""
            while True:
                value += data[1:5]
                length += 5
                if data[0] == "0":
                    data = data[5:]
                    break
                else:
                    data = data[5:]
            value = int(value, 2)

        case _:  # operator
            length_type = data[0]
            if length_type == "0":
                subpacket_length = int(data[1:16], 2)
                length += 16
                data = data[16:]
                used = 0
                while used < subpacket_length:
                    subpacket = parse_packet(data)
                    data = data[subpacket.length:]
                    used += subpacket.length
                    length += subpacket.length
                    subpackets.append(subpacket)
            else:
                packet_count = int(data[1:12], 2)
                data = data[12:]
                length += 12
                for _ in range(packet_count):
                    subpacket = parse_packet(data)
                    data = data[subpacket.length:]
                    length += subpacket.length
                    subpackets.append(subpacket)

    return Packet(version, type, length, value, subpackets)


def sum_version(packet):
    sum = packet.version
    for subpacket in packet.subpackets:
        sum += sum_version(subpacket)
    return sum


def run(input, title):
    print(title)
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

    packet = parse_packet(data)
    sum = sum_version(packet)
    print(f"Version sum: {sum}")


def main():
    example = read_input_from_file("day-16/example.txt")
    input = read_input_from_file("day-16/input.txt")

    for e in example:
        run([e], f"example {e}")

    run(input, "puzzle data")


if __name__ == "__main__":
    main()
