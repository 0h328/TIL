import sys
sys.stdin = open('input.txt')



for tc in range(1, 11):
    length = int(input())
    board = [input() for _ in range(8)]
    board.extend(map(lambda x: ''.join(x), zip(*board)))
    answer = 0

    for e in board:
        for i in range(9-length):
            tmp = e[i:i+length]
            if tmp == tmp[::-1]:
                answer += 1

    print('#{} {}'.format(tc, answer))