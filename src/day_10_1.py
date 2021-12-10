def main():
    lines = []
    with open('../input/input_day_10.in') as f:
        lines = f.readlines()
        lines = list(map(lambda line: line.strip(), lines))

    error_score = 0
    completion_scores = []
    for line in lines:
        signs = []
        line_finished = False
        completion_score = 0

        for sign in line:
            if not line_finished:
                if sign == '(':
                    signs.append('(')
                if sign == '[':
                    signs.append('[')
                if sign == '{':
                    signs.append('{')
                if sign == '<':
                    signs.append('<')
                if sign == ')':
                    if signs.pop() != '(':
                        error_score += 3
                        line_finished = True
                if sign == ']':
                    if signs.pop() != '[':
                        error_score += 57
                        line_finished = True
                if sign == '}':
                    if signs.pop() != '{':
                        error_score += 1197
                        line_finished = True
                if sign == '>':
                    if signs.pop() != '<':
                        error_score += 25137
                        line_finished = True

    print(error_score)


if __name__ == '__main__':
    main()
