import sys

sys.stdin = open('input.txt')


def dfs(num):
    visited[num] = 1  # 해당 조로 묶인 사람 체크
    for i in groups[num]:
        if not visited[i]:
            dfs(i)


T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())  # N: 출석번호마지막, M: 신청서 개수
    m = list(map(int, input().split()))
    groups = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    cnt = 0

    for i in range(M):  # 신청한 사람, 신청당한 사람 모두 처리해줘야 함
        groups[m[i * 2]].append(m[i * 2 + 1])
        groups[m[i * 2 + 1]].append(m[i * 2])
    print(groups)
    for i in range(1, N + 1):
        if not visited[i]:
            cnt += 1
            dfs(i)
            print(visited)

    print('#{} {}'.format(t, cnt))
