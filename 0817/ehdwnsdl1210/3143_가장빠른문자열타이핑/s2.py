import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    pa = input()
    ty = input()

    m = len(pa)
    n = len(ty)

    # text에서 pattern이 존재 가능한 모든 시작 위치
    ans = 0
    for i in range(0, n-m+1):
        # 패턴의 길이 m 만큼 비교

        for j in range(m):      # j는 0 ~ m-1
            if pa[j] != ty[i+j]:
                break
        else:
            ans = 1
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