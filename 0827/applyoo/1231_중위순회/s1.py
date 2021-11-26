import sys
sys.stdin = open('input.txt')


def in_order(n):  # 중위순회
    global ans
    if n:
        in_order(le[n])  # 왼쪽으로 진행
        ans += a[n-1][1]  # 현재 노드 값 더해줌
        in_order(ri[n])  # 오른쪽으로 진행


for test in range(10):
    N = int(input())
    a = [input().split() for _ in range(N)]
    le = [0] * (N+1)  # 왼쪽 자식 노드 번호
    ri = [0] * (N+1)  # 오른쪽 자식 노드 번호
    ans = ''

    for p, v, *c in a:
        if c:
            p = int(p)  # 문자 -> 정수
            le[p] = int(c[0])
            if len(c) == 2:  # 길이가 2라면 왼쪽, 오른쪽 자식이 있는 것
                ri[p] = int(c[1])

    in_order(1)  # 1부터 시작(루트 노드는 무조건 1이므로)
    print('#{} {}'.format(test+1, ans))
