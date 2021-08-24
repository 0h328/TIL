import sys

sys.stdin = open('input.txt')

for test in range(1, 1 + int(input())):
    data = [input() for _ in range(5)]

    answer = ''

    max_list = []
    for i in data:
        max_list.append(len(i))

    for i in range(max(max_list)):
        for j in range(max(max_list)):
            try:
                answer += data[j][i]
            except:
                continue

    print('#{} {}'.format(test, answer))
