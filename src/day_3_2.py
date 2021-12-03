import copy


def main(name):
    lines = []
    with open('../input/input_day_3.in') as f:
        lines = f.readlines()

    oxygen_rating = copy.deepcopy(lines)
    scrub_rating = copy.deepcopy(lines)

    input_length = len(oxygen_rating[0][:-1])

    for position in range(0, input_length):
        if len(oxygen_rating) != 1:
            common_bit = get_most_common_column_bit(oxygen_rating, position)
            oxygen_rating = list(filter(lambda x: x[position] == common_bit, oxygen_rating))

    for position in range(0, input_length):
        if len(scrub_rating) != 1:
            common_bit = get_least_common_column_bit(scrub_rating, position)
            scrub_rating = list(filter(lambda x: x[position] == common_bit, scrub_rating))

    oxygen_rating = oxygen_rating[0]
    scrub_rating = scrub_rating[0]

    print(int(oxygen_rating, 2) * int(scrub_rating, 2))


def get_most_common_column_bit(matrix, column):
    ones_in_lines = 0
    for line in matrix:
        if line[column] == '1':
            ones_in_lines += 1

    return '1' if ones_in_lines >= len(matrix) / 2 else '0'


def get_least_common_column_bit(matrix, column):
    ones_in_lines = 0
    for line in matrix:
        if line[column] == '1':
            ones_in_lines += 1

    return '0' if ones_in_lines >= len(matrix) / 2 else '1'


if __name__ == '__main__':
    main('PyCharm')

