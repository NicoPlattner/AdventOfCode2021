def main(name):
    lines = []
    with open('../input/input_day_4.in') as f:
        lines = f.readlines()

    guesses = list(map(lambda guess: int(guess), lines[0].split(',')))
    boards = []
    marked = []
    won_board_indizes = []
    won_boards = []
    won_marked = []
    won = -1

    current_board = -1
    for count, line in enumerate(lines[1:-1]):
        if len(line) == 1:
            boards.append([])
            marked.append([])
            current_board += 1
        else:
            line = line.strip()
            boards[current_board].append(list(map(lambda num: int(num), filter(lambda l: l != '', line.split(' ')))))
            marked[current_board].append([False, False, False, False, False])

    finished = False
    for guess in guesses:
        for board_count, board in enumerate(boards):
            for line_count, line in enumerate(board):
                for num_count, num in enumerate(line):
                    if len(won_boards) < len(boards):
                        if num == guess:
                            marked[board_count][line_count][num_count] = True

                            if check_if_finished(marked[board_count], line_count, num_count):
                                if board_count not in won_board_indizes:
                                    won = guess
                                    won_board_indizes.append(board_count)
                                    won_boards.append(board)
                                    won_marked.append(marked[board_count])

    print(get_sum_of_not_guessed(won_boards[-1], won_marked[-1]) * won)

def get_sum_of_not_guessed(board, marked):
    sum = 0

    for line_count, line in enumerate(board):
        for num_count, num in enumerate(line):
            if not marked[line_count][num_count]:
                sum += num

    return sum


def check_if_finished(marked, line_count, num_count):
    finished_line = True
    finished_col = True
    for lc, line in enumerate(marked):
        if lc == line_count:
            for marking in line:
                if not marking:
                    finished_line = False
        else:
            if not line[num_count]:
                finished_col = False

    return finished_line or finished_col

if __name__ == '__main__':
    main('PyCharm')

