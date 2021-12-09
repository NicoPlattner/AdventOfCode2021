import statistics


def main(name):
    lines = []
    with open('../input/input_day_9.in') as f:
        lines = f.readlines()
        lines = list(map(lambda line: line.strip(), lines))

    sum_risk_levels = 0
    for line_count, line in enumerate(lines):
        for position_count, position in enumerate(line):
            left_lower = False
            up_lower = False
            right_lower = False
            down_lower = False

            if (position_count != 0 and line[position_count - 1] > position) or position_count == 0:
                left_lower = True

            if(line_count != 0 and lines[line_count - 1][position_count] > position) or line_count == 0:
                up_lower = True

            if (position_count != len(line) - 1 and line[position_count + 1] > position) or position_count == len(line) - 1:
                right_lower = True

            if(line_count != len(lines) - 1 and lines[line_count + 1][position_count] > position) or line_count == len(lines) - 1:
                down_lower = True

            if left_lower and up_lower and right_lower and down_lower:
                sum_risk_levels += int(position) + 1

    print(sum_risk_levels)


if __name__ == '__main__':
    main('PyCharm')
