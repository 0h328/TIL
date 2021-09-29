import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    data.sort()
    num = deque(data)

    ans = []

    for _ in range(N//2):
        ans.append(num.pop())
        ans.append(num.popleft())

    print('#{} {}'.format(tc, ' '.join(map(str, ans[:10]))))