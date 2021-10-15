def bfs():
    Q = deque()
    Q.append(N)
    memo[N] = True

    ans = 0

    while Q:
        size = len(Q)

        for i in range(size):
            num = Q.popleft()
            if num == M:
                return ans

            for j in (num+1, num-1, num*2, num-10):
                if 0 < j <= 1000000 and not memo[j]:
                    memo[j] = True
                    Q.append(j)

        ans += 1


# Q 사이즈로 묶는 방법
import sys
sys.stdin = open('input.txt')
from collections import deque
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())                            # N을 M으로 바꾸는 최소한의 연산수
    memo = [False] * 1000001                                     # 10000001인 이유 -> 1 ~ 100만까지 사용 가능하기 때문
    print('#{} {}'.format(tc, bfs()))