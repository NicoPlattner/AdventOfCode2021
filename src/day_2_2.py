def main(name):
    lines = []
    with open('../input/input_day_2.in') as f:
        lines = f.readlines()

    aim = 0
    x = 0
    depth = 0
    for line in lines:
        command = line.split()[0]
        distance = int(line.split()[1])

        if command == 'forward':
            x += distance
            depth += aim * distance
        elif command == 'up':
            aim -= distance
        elif command == 'down':
            aim += distance

    print(x * depth)


if __name__ == '__main__':
    main('PyCharm')

