def main(name):
    fish = []
    with open('../input/input_day_6.in') as f:
        lines = f.readlines()
        lines[0] = lines[0].strip()
        fish = lines[0].split(',')
        fish = list(map(lambda char: int(char), fish))

    for day in range(0, 80):
        amount_fish = len(fish)

        for fish_idx in range(0, amount_fish):
            fish[fish_idx] -= 1

            if fish[fish_idx] < 0:
                fish[fish_idx] = 6
                fish.append(8)

    print(len(fish))


if __name__ == '__main__':
    main('PyCharm')
