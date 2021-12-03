def main(name):
    lines = []
    with open('../input/input_day_3.in') as f:
        lines = f.readlines()

    ones_in_lines = []
    for line in lines:
        for count, char in enumerate(line[:-1]):
            if len(ones_in_lines) <= count:
                ones_in_lines.append(0)

            if char == '1':
                ones_in_lines[count] += 1

    gamma_binary = ''
    epsilon_binary = ''
    for num in ones_in_lines:
        if num > len(lines) / 2:
            gamma_binary += '1'
            epsilon_binary += '0'
        else:
            gamma_binary += '0'
            epsilon_binary += '1'

    print(int(gamma_binary, 2) * int(epsilon_binary, 2))


if __name__ == '__main__':
    main('PyCharm')

