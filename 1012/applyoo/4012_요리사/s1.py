import sys
sys.stdin = open('input.txt')


def cal(a):  # 두 요리의 차를 계산하는 함수
    b = list(set([i for i in range(N)]) - set(a))

    a_s = b_s = 0
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            a_s += (A[a[i]][a[j]] + A[a[j]][a[i]])  # a 계산
            b_s += (A[b[i]][b[j]] + A[b[j]][b[i]])  # b 계산
    return abs(a_s - b_s)


def dfs(foods):
    global ans
    if len(foods) == N // 2:  # base case
        ans = min(ans, cal(foods))
        return

    for i in range(max(foods) + 1, N):
        foods.append(i)
        dfs(foods)  # 백트래킹
        foods.pop()


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    ans = 10 ** 7  # 문제상 최댓값 고려

    dfs([0])  # 0은 미리 포함되어도 결과에는 상관 없음(시간 단축)
    print('#{0} {1}'.format(tc, ans))
