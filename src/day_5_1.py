def main(name):
    lines = []
    with open('../input/input_day_5.in') as f:
        lines = f.readlines()
        lines = list(map(lambda l: l.strip(), lines))

    lines = list(map(lambda l: l.split(' -> '), lines))
    field = [[0] * 1000 for _ in range(1000)]

    for count, line in enumerate(lines):
        coord1 = line[0].split(',')
        coord1 = list(map(lambda num: int(num), coord1))
        coord2 = line[1].split(',')
        coord2 = list(map(lambda num: int(num), coord2))

        if coord1[0] == coord2[0] or coord1[1] == coord2[1]:
            x1, x2 = sorted((coord1[0], coord2[0]))
            for x in range(x1, x2 + 1):
                y1, y2 = sorted((coord1[1], coord2[1]))
                for y in range(y1, y2 + 1):
                    field[x][y] += 1

    amount_dangerous = 0
    for y in field:
        for x in y:
            if x >= 2:
                amount_dangerous += 1
    print(amount_dangerous)


if __name__ == '__main__':
    main('PyCharm')

