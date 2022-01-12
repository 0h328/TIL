from collections import deque
from itertools import permutations
import sys
sys.stdin = open('input.txt')

# c->a,b / b->a,c / a->b,c
def bfs():
    q = deque()
    q.append((0, 0, C))

    while q:
        a, b, c = q.popleft()

        if not check[a][b]: # a와 b에 옮기지 않은 경우만 체크
            check[a][b] = 1

            if a == 0:          # a가 0일 때
                res.append(c)   # c의 값 추가

            if c+a > A: # c->a
                q.append((A, b, c+a-A))
            else:
                q.append((c+a, b, 0))

            if c+b > B: # c->b
                q.append((a, B, c+b-B))
            else:
                q.append((a, c+b, 0))

            if b+a > B: # b->a
                q.append((a+b-B, B, c))
            else:
                q.append((0, b+a, c))

            if b+c > C: # b->c
                q.append((a, b+c-C, C))
            else:
                q.append((a, 0, b+c))

            if a+b > A: # a->b
                q.append((A, b+a-A, c))
            else:
                q.append((a+b, 0, c))

            if a+c > C: # a->c
                q.append((a+c-C, b, C))
            else:
                q.append((0, b, a+c))


A, B, C = map(int, sys.stdin.readline().split()) # C는 전체 합(기본값)
# k = list(permutations([0, 1, 2], 2))
check = [[0] * 201 for _ in range(201)]
res = []
bfs()
res.sort()
for i in range(len(res)):
    print(res[i], end=' ')