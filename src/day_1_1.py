def main(name):
    lines = []
    with open('../input/input_day_1.in') as f:
        lines = f.readlines()

    amount_rising_nums = 0
    for count, line in enumerate(lines):
        if count > 0 and int(lines[count - 1]) < int(line):
            amount_rising_nums += 1

    print(amount_rising_nums)


if __name__ == '__main__':
    main('PyCharm')
