import sys

sys.stdin = open('input.txt')

for test in range(1, 1 + int(input())):
    N, M = list(map(int, input().split()))

    data = list(map(int, input().split()))

    for i in range(M):
        data.append(data.pop(0))

    print('#{} {}'.format(test, data[0]))
