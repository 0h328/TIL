import sys
sys.stdin = open('input.txt')


def babygin(p, n):                      # 이번에 추가될 숫자에 대한 검사
    if n in p:                          # list에 이미 같은 숫자가 있다면
        if p.count(n) == 2:             # 기존에 그 숫자가 2개 있었다면 = triplet
            return True
    else:                               # list에 같은 숫자가 없었다면
        if n-1 in p:                    # n-1이 있었으면 (n-2, n-1, n) 이거나 (n-1, n, n+1)
            if n-2 in p or n+1 in p:
                return True
        elif n+1 in p and n+2 in p:     # n-1이 없었으면 남은 경우는 (n, n+1, n+2)
            return True
    p.append(n)                         # 확인 작업 다 끝나고 다음 턴을 위해 추가
    return False                        # 중간에 안 걸렸으면 무조건 false


T = int(input())
for t in range(1, T+1):
    p1, p2 = [], []
    num = list(map(int, input().split()))
    ans = 0

    for i in range(12):                             # 숫자 추가하면서 바로 babygin 확인
        if i % 2 == 0 and babygin(p1, num[i]):
            ans = 1
            break
        elif i % 2 == 1 and babygin(p2, num[i]):
            ans = 2
            break

    print('#{} {}'.format(t, ans))