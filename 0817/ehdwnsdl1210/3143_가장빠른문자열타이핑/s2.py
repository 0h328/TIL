import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    p = input() # 찾을려는
    t = input() # 전체

    m = len(p)
    n = len(t)

    # text에서 pattern이 존재 가능한 모든 시작 위치
    ans = 0
    for i in range(0, n-m+1):
        # 패턴의 길이 m 만큼 비교

        for j in range(m):      # j는 0 ~ m-1
            if p[j] != t[i+j]:
                found = False
                break
        else:
            ans = 1
            break
    print(ans)

    # # text에서 pattern이 존재 가능한 모든 시작 위치
    # for i in range(0, n - m + 1):
    #     # 패턴의 길이 m 만큼 비교
    #     j = 0
    #     while j < m:        # j는 0 ~ m-1
    #         if p[j] != t[i + j]:
    #             found = False
    #             break
    #         j += 1
    #     if j == m: