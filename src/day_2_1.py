def main(name):
    lines = []
    with open('../input/input_day_2.in') as f:
        lines = f.readlines()

    x = 0
    depth = 0
    for line in lines:
        command = line.split()[0]
        distance = int(line.split()[1])

        if command == 'forward':
            x += distance
        elif command == 'up':
            depth -= distance
        elif command == 'down':
            depth += distance

    print(x * depth)


if __name__ == '__main__':
    main('PyCharm')

