import sys
sys.stdin = open('input.txt', encoding='UTF-8')

for _ in range(10):
    n = int(input())
    p = input()
    t = input()

    i = 0
    cnt = 0

    while i < len(t):
        j = 0
        while j < len(p):
            if i == len(t):                 # 무한루프 방지 IndexError 방지
                break
            if t[i] != p[j]:
                i -= j
                j = -1
            i += 1
            j += 1                          # j가 len(p)가 된 것은, p랑 t안에 p가 동일한 것을 찾았기 때문

        if i != len(t):
            cnt += 1
        elif j == len(p) and i == len(t):
            # j == len(p)의 의미. t 내 p를 찾은 거임.
            # i == len(t)는 마지막 문자가 되었으므로
            cnt += 1

    print('#{} {}'.format(n, cnt))






