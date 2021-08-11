import sys
sys.stdin = open('input.txt')


for tc in range(10):                    # 10개의 tc
    N = int(input())                    # 덤프 횟수
    L = list(map(int, input().split())) # 숫자들 찢어주고

    for _ in range(N):                  # 덤프동안
        L[L.index(max(L))] -= 1         # 최대는 계속 1줄고
        L[L.index(min(L))] += 1         # 최소는 계속 1늘고

    print('#{} {}'.format(tc+1, max(L) - min(L)))