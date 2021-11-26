# from collections import deque
import sys
sys.stdin = open('input.txt')


for t in range(10):
    tc = int(input())
    data = list(map(int, input().split()))
    minus = 1

    while True:
        # que = deque()
        # for i in range(len(data)):
        #     que.append(data[i])
        # num = que.popleft()
        num = data.pop(0)
        if num - minus <= 0:
            data.append(0)  # 0이하인경우 0으로 유지
            break
        else:
            data.append(num - minus)
        minus += 1

        if minus > 5:
            minus = 1
    print('#{}'.format(tc), end = ' ')
    print(*data)
