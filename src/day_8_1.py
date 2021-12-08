import statistics


def main(name):
    lines = []
    with open('../input/input_day_8.in') as f:
        lines = f.readlines()
        lines = list(map(lambda line: line.strip(), lines))

    inputs = list(map(lambda line: line.split(' '), lines))

    sum_outputs = 0
    for inp in inputs:
        numbers = ['', '', '', '', '', '', '', '', '', '']
        segments = {
            'top': '',
            'top_left': '',
            'top_right': '',
            'center': '',
            'bottom_left': '',
            'bottom_right': '',
            'bottom': '',
        }

        for i in range(0, 10):
            if len(inp[i]) == 2:
                numbers[1] = "".join(sorted(inp[i]))
            elif len(inp[i]) == 3:
                numbers[7] = "".join(sorted(inp[i]))
            elif len(inp[i]) == 4:
                numbers[4] = "".join(sorted(inp[i]))
            elif len(inp[i]) == 7:
                numbers[8] = "".join(sorted(inp[i]))

        segments['top'] = get_single_different_segment(numbers[1], numbers[7])
        numbers[9] = get_number_nine(inp[0:10], numbers[4])
        segments['bottom'] = get_single_different_segment(numbers[4] + segments['top'], numbers[9])
        segments['bottom_left'] = get_single_missing_segment(numbers[9])
        numbers[3] = get_three(inp[0:10], numbers[1])
        segments['center'] = get_single_different_segment(numbers[7] + segments['bottom'], numbers[3])
        numbers[0] = numbers[8].replace(segments['center'], '')
        numbers[6] = "".join(sorted(list(filter(lambda num: len(num) == 6, get_remaining_unknowns(inp[0:10], numbers)))[0]))
        numbers[2] = "".join(sorted(list(filter(lambda num: segments['bottom_left'] in num, get_remaining_unknowns(inp[0:10], numbers)))[0]))
        numbers[5] = "".join(sorted(get_remaining_unknowns(inp[0:10], numbers)[0]))

        output = ''

        for i in range(11, 15):
            output_string_sorted = "".join(list(map(lambda n: str(n), sorted(inp[i]))))
            output += str(numbers.index(output_string_sorted))

        sum_outputs += int(output)

    print(sum_outputs)


def get_three(inputs, one):
    for inp in inputs:
        if len(inp) == 5 and segment_contains_segment(inp, one):
            return "".join(sorted(inp))


def get_single_different_segment(num1, num2):
    first_set = set(num1)
    second_set = set(num2)
    difference = first_set.symmetric_difference(second_set)
    return difference.pop()


def get_single_not_contained_segment(bigger, smaller):
    for segment in smaller:
        if segment not in bigger:
            return segment


def get_single_missing_segment(num):
    return get_single_different_segment('abcdefg', num)


def get_number_nine(inputs, four):
    for inp in inputs:
        if len(inp) == 6 and segment_contains_segment(inp, four):
            return "".join(sorted(inp))


def segment_contains_segment(bigger, smaller):
    for segment in smaller:
        if segment not in bigger:
            return False
    return True


def get_remaining_unknowns(inputs, known_numbers):
    unknown = []

    for inp in inputs:
        if "".join(sorted(inp)) not in known_numbers:
            unknown.append("".join(sorted(inp)))

    return unknown


if __name__ == '__main__':
    main('PyCharm')
