import statistics


def main(name):
    lines = []
    with open('../input/input_day_7.in') as f:
        lines = f.readlines()

    positions = lines[0].split(',')
    positions = list(map(lambda p: int(p), positions))

    max_position = max(positions)
    fuel_consumptions = []

    print(max_position)

    for i in range(0, max_position + 1):
        s = 0

        for position in positions:
            s += sum(range(0, abs(position - i) + 1))

        fuel_consumptions.append(s)

    print(fuel_consumptions)
    print(min(fuel_consumptions))


if __name__ == '__main__':
    main('PyCharm')
