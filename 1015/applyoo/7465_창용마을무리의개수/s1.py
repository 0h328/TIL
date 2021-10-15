import sys
sys.stdin=open('input.txt')


def find(x):  # 루트 노드를 찾는 함수
    if p[x] < 0: return x
    p[x] = find(p[x])
    return p[x]


def union(x, y):  # 더 큰 집합(트리)에 합치는 함수
    x, y = find(x), find(y)

    if x != y:
        if p[x] <= p[y]:
            p[x] += p[y]
            p[y] = x
        else:
            p[y] += p[x]
            p[x] = y


ans = []
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    p = [-1] * (N + 1)  # 음수 => 루트 노드임을 의미 & 양수로 바꾸면 해당 집합의 개수
    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)

    ans.append('#{} {}'.format(tc, len([i for i in p[1:] if i < 0])))  # 음수의 개수를 반환

print(*ans, sep='\n')
