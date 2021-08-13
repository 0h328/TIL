import sys
sys.stdin = open('input.txt')

def pageSearch(l, r, cnt, p):
    if l > r: # 못 찾고 범위 넘기면 최대값 반환
        return 1000
    c = (l+r) // 2
    if c == p: # 찾으면 바로 cnt 반환
        return cnt
    else:
        if c > p:
            return pageSearch(l, c, cnt + 1, p)
        else:
            return pageSearch(c, r, cnt + 1, p)

T = int(input())

for t in range(1, T+1):
    P, A, B = map(int, input().split())
    A_cnt = pageSearch(1, P, 0, A)
    B_cnt = pageSearch(1, P, 0, B)

    if A_cnt > B_cnt:
        print('#{} {}'.format(t, 'B'))
    elif A_cnt < B_cnt:
        print('#{} {}'.format(t, 'A'))
    else:
        print('#{} {}'.format(t, '0'))