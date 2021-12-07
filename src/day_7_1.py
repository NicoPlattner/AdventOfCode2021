import statistics


def main(name):
    lines = []
    with open('../input/input_day_7.in') as f:
        lines = f.readlines()

    positions = lines[0].split(',')
    positions = list(map(lambda p: int(p), positions))

    median = statistics.median(positions)

    fuel_consumption = 0
    for position in positions:
        fuel_consumption += abs(median - position)

    print(int(fuel_consumption))


if __name__ == '__main__':
    main('PyCharm')
