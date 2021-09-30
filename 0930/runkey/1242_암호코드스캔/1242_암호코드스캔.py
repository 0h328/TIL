# import sys
# sys.stdin = open('sample.txt', 'r')
def erases(i, j, ratio):
    cnt = j
    while arrb[cnt][j] == 1:
        cnt += 1
    for r in range(i, cnt):
        for c in range(j - 56 * ratio + 1, j + 1):
            arrb[r][c] = 0

h2b = {'0' : '0000',
       '1' : '0001',
       '2' : '0010',
       '3' : '0011',
       '4' : '0100',
       '5' : '0101',
       '6' : '0110',
       '7' : '0111',
       '8' : '1000',
       '9' : '1001',
       'A' : '1010',
       'B' : '1011',
       'C' : '1100',
       'D' : '1101',
       'E' : '1110',
       'F' : '1111',
       }

pwd = {211:0,
       221:1,
       122:2,
       411:3,
       132:4,
       231:5,
       114:6,
       312:7,
       213:8,
       112:9,
       }



T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arrh = [input() for _ in range(N)]
    arrb = [''] * N
    for i in range(N):
        for j in range(M):
            for k in range(4)
                arrb[i][j*4 + k] += int(h2b[arrh[i][j][k]]) # 16진수 -> 비트패턴

    # 암호패턴의 끝 위치 찾기
    M *= 4
    for i in range(N):
        j = M - 1
        num = [0] * 8
        k = 0       # 찾은 암호숫자의 갯수
        while j >= 0:
            while j >= 0 and arrb[i][j] == 0:    # 1을 만날 때 까지 이동, (암호 패턴의 끝)
                j -= 1
            c1 = 0
            if k == 0:
                col = j         # 패턴의 끝
            while j >= 0 and arrb[i][j] == 1:
                c1 += 1
                j -= 1
            c2 = 0
            while j >= 0 and arrb[i][j] == 0:
                c2 += 1
                j -= 1
            c3 = 0
            while j >= 0 and arrb[i][j] == 1:
                c3 += 1
                j -= 1
            if c1 > 0:
                ratio = min(c1, c2, c3)
                num[7 - k] = pwd[c3 * 100 + c2 * 10 + c1]
                k += 1
                if k == 8:
                    print(ratio)
                    print(*num)

                erase = (i, col, ratio)