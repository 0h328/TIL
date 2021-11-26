import sys
from collections import deque
sys.stdin = open('input.txt')

T = 10

for _ in range(T):
    tc = int(input())
    front = -1

    data = list(map(int, input().split()))
    # data = deque(data)
    sub_val = 1
    while True:
        # temp = data.popleft() - sub_val
        front += 1
        temp = data[front] - sub_val

        if temp <= 0:
            temp = 0
        data.append(temp)

        if not temp:
            break

        sub_val += 1
        if sub_val > 5:
            sub_val %= 5

    print('#{}'.format(tc), end=' ')
    print(*data[front+1:])