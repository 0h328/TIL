import sys

sys.stdin = open('input.txt')

for test in range(1, 1 + int(input())):
    data = [0] * 5001
    for i in range(int(input())):
        x, y = map(int, input().split())
        for j in range(x, y + 1):
            data[j] += 1
    answer = [str(data[int(input())]) for _ in range(int(input()))]
    print('#{} {}'.format(test, ' '.join(answer)))

