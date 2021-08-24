import sys
sys.stdin = open('input.txt')

t = int(input())
for num in range(1,t+1):
    n, k = map(int, input().split())
    l = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for sub in [*l, *list(zip(*l))]:
        # 최장 1길이 찾기
        i = 0
        length = 0
        while i < n:
            while i < n and sub[i] == 1:
                length += 1
                i += 1
            if length == k:
                cnt += 1
            length = 0
            i += 1
    print('#{} {}'.format(num, cnt))




