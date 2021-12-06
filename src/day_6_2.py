from collections import Counter

def main(name):
    fish = []
    fish_numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    with open('../input/input_day_6.in') as f:
        lines = f.readlines()
        lines[0] = lines[0].strip()
        fish = lines[0].split(',')
        fish = list(map(lambda char: int(char), fish))

    fish_numbers[1] = Counter(fish)[1]
    fish_numbers[2] = Counter(fish)[2]
    fish_numbers[3] = Counter(fish)[3]
    fish_numbers[4] = Counter(fish)[4]
    fish_numbers[5] = Counter(fish)[5]

    for day in range(0, 256):
        temp1 = fish_numbers[8]
        temp2 = fish_numbers[7]
        for i in range(8, -1, -1):
            if i != 0:
                temp2 = fish_numbers[i - 1]
                fish_numbers[i - 1] = temp1
                temp1 = temp2
            else:
                fish_numbers[8] = temp1
                fish_numbers[6] += temp1

    print(sum(fish_numbers))


if __name__ == '__main__':
    main('PyCharm')
