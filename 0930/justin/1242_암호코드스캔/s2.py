P = {(2, 1, 1): 0,
     (2, 2, 1): 1,
     (1, 2, 2): 2,
     (4, 1, 1): 3,
     (1, 3, 2): 4,
     (2, 3, 1): 5,
     (1, 1, 4): 6,
     (3, 1, 2): 7,
     (2, 1, 3): 8,
     (1, 1, 2): 9}

A = ord('A')
nine, zero = ord('9'), ord('0')
arr = [[0] * 2000 for _ in range(2000)]

def solve():
    ret = 0
    for i in range(N):
        j = M * 4 - 1
        while j >= 0:
            if arr[i][j] == 1 and arr[i - 1][j] == 0:
                pwd = []
                MIN = 0
                for k in range(8):
                    c2 = c3 = c4 = 0
                    while arr[i][j] == 0: j -= 1
                    while arr[i][j] == 1: c4, j = c4 + 1, j - 1
                    while arr[i][j] == 0: c3, j = c3 + 1, j - 1
                    while arr[i][j] == 1: c2, j = c2 + 1, j - 1
                    if k == 0:
                        MIN = min(c2, c3, c4)
                    pwd.append(P[(c2 // MIN, c3 // MIN, c4 // MIN)])
                a = pwd[0] + pwd[2] + pwd[4] + pwd[6]
                b = pwd[1] + pwd[3] + pwd[5] + pwd[7]
                if ((b * 3 + a) % 10) == 0:
                    ret += (a + b)
            j -= 1
    return ret

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    for i in range(N):
        tmp = input()
        for j in range(M):
            t = ord(tmp[j])
            val = (t - A) + 10 if t > nine else t - zero
            arr[i][j*4] = 1 if val & 0x8 else 0
            arr[i][j*4+1] = 1 if val & 0x4 else 0
            arr[i][j*4+2] = 1 if val & 0x2 else 0
            arr[i][j*4+3] = 1 if val & 0x1 else 0
    ans = solve()
    print('#{} {}'.format(tc, ans))