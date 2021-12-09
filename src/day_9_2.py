import statistics


def main(name):
    lines = []
    with open('../input/input_day_9.in') as f:
        lines = f.readlines()
        lines = list(map(lambda line: line.strip(), lines))

    basin_sizes = []
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
                basin_sizes.append(get_basin_size(lines, position_count, line_count))

    basin_sizes = sorted(basin_sizes, reverse=True)
    print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])


def get_basin_size(field, x, y):
    basin = []
    basin.append([x, y])

    for position in basin:
        if check_step(field, position[0], position[1], 1, 0, basin):
            basin.append([position[0] + 1, position[1]])
        if check_step(field, position[0], position[1], -1, 0, basin):
            basin.append([position[0] - 1, position[1]])
        if check_step(field, position[0], position[1], 0, 1, basin):
            basin.append([position[0], position[1] + 1])
        if check_step(field, position[0], position[1], 0, -1, basin):
            basin.append([position[0], position[1] - 1])

    return len(basin)


def check_step(field, x, y, delta_x, delta_y, basin):
    if 0 > x + delta_x or len(field[0]) <= x + delta_x or 0 > y + delta_y or len(field) <= y + delta_y:
        return False

    if field[y + delta_y][x + delta_x] == '9':
        return False

    if [x + delta_x, y + delta_y] in basin:
        return False

    return True


if __name__ == '__main__':
    main('PyCharm')
