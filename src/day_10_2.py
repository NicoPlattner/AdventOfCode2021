def main():
    lines = []
    with open('../input/input_day_10.in') as f:
        lines = f.readlines()
        lines = list(map(lambda line: line.strip(), lines))

    error_score = 0
    completion_scores = []
    for line in lines:
        signs = []
        error = False
        completion_score = 0

        for sign in line:
            if not error:
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
                        error = True
                if sign == ']':
                    if signs.pop() != '[':
                        error_score += 57
                        error = True
                if sign == '}':
                    if signs.pop() != '{':
                        error_score += 1197
                        error = True
                if sign == '>':
                    if signs.pop() != '<':
                        error_score += 25137
                        error = True

        if not error:
            for sign in reversed(signs):
                completion_score *= 5

                if sign == '(':
                    completion_score += 1
                if sign == '[':
                    completion_score += 2
                if sign == '{':
                    completion_score += 3
                if sign == '<':
                    completion_score += 4

            completion_scores.append(completion_score)

    middle_index = int(len(completion_scores) / 2)
    print(sorted(completion_scores)[middle_index])


if __name__ == '__main__':
    main()
