# 상준님 풀이
test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    ans = [[0] * n for _ in range(n)]
    dr = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    num, cnt, check = 1, n, 0  # 채워넣을 숫자, 채워넣을 칸수, 채워넣은 줄의 개수
    x, y = -1, 0               # 시작점

    while cnt:

        if check % 2:          # 방향전환 후 개수 줄어듬
            cnt -= 1

        for i in range(cnt):   # 리스트를 채워넣을 칸수만큼 채워넣음
            x += dr[check % 4][0]
            y += dr[check % 4][1]
            ans[y][x] = num
            num += 1

        check += 1             # 채워넣은 줄의 개수 추가

    print("#{}".format(test))

    for row in ans:
        print(" ".join(map(str, row)))