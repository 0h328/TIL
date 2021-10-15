import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())        # N: 총원 , M: 신청서
    arr = list(map(int, input().split()))
    parent = list(range(N+1))

    def find_set(x):
        if x == parent[x]:
            return x
        return find_set(parent[x])

    for i in range(M):
        x = arr[2*i]; y = arr[2*i+1]
        parent[find_set(y)] = find_set(x)  # y의 대표 원소를 x의 대표원소로 교체

    ans = 0
    for i in range(1, N+1):                # 대표 원소가 자기 자신인 경우의 수 체크
        if parent[i] == i:
            ans += 1
    print('#{} {}'.format(tc, ans))
