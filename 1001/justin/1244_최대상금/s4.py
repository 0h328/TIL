def swap(n, i, j):
    a = (n // weights[i]) % 10
    b = (n // weights[j]) % 10
    return n - a * weights[i] + a * weights[j] - b * weights[j] + b * weights[i]

from collections import deque
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    cards, cnt = input().split()                 # cards: 숫자판의 정보(문자열), cnt: 최대 교환 횟수
    N = len(cards)
    num, cnt = int(cards), int(cnt)
    visited = [[] for _ in range(12)]
    weights = [1, 10, 100, 1000, 10000, 100000]  # 상금 수여에 부여되는 가중치 -> *10
    ans = 0
    Q = deque()
    Q.append((num, 0))

    while Q:
        n, k = Q.popleft()
        if k == cnt:
            ans = max(ans, n)
        else:
            for i in range(N-1):
                for j in range(i+1, N):
                    val = swap(n, i, j)
                    if val in visited[k+1]: continue        # 이미 체크한 값이면 넘어가자
                    visited[k+1].append(val)
                    Q.append((val, k+1))

    print('#{} {}'.format(tc, ans))