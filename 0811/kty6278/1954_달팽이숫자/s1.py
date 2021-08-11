# input 데이터를 불러온다.
import sys
sys.stdin = open('input.txt')

testcase = int(input())

for test in range(testcase):
    num = int(input())
    for _ in range(num):
        snail = [0] * num
        # print(snail)

        di = [0, 1, 0, -1]
        dj = [1, 0, -1, 0]

        i, j = 0, -1
        k = 0

        cnt = 1

        while cnt <= i ** 2:
            ni, nj = i + di[k], j + dj[k]

            if num > ni >= 0 and num > nj >= 0 and snail[ni][nj] == 0:
                snail[ni][nj] = cnt
                cnt += 1
                i, j = ni, nj
            else:
                k = (k + 1) % 4
        print(snail)