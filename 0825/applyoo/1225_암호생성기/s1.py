import sys
sys.stdin = open('input.txt')

from collections import deque

for test in range(10):
    N = int(input())
    arr = deque(map(int, input().split()))
    go = True  # while 실행/종료 변수

    while go:
        for i in range(1, 6):
            if arr[0] - i > 0:
                arr.append(arr.popleft()-i)  # pop해서 뺀 것을 추가해주기
            else:
                arr.popleft()  # pop
                arr.append(0)  # 0 추가
                go = False
                break

    print('#{}'.format(test+1), end=' ')
    print(*arr)
