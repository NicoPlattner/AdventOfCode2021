def main(name):
    lines = []
    with open('../input/input_day_1.in') as f:
        lines = f.readlines()

    amount_rising_sums = 0
    for count, line in enumerate(lines):
        if count > 2:
            sum1 = int(lines[count - 3]) + int(lines[count - 2]) + int(lines[count - 1])
            sum2 = int(lines[count - 2]) + int(lines[count - 1]) + int(line)

            if sum1 < sum2:
                amount_rising_sums += 1

    print(amount_rising_sums)

if __name__ == '__main__':
    main('PyCharm')

