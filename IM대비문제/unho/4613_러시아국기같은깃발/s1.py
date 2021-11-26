import sys
sys.stdin = open('input.txt')

test_case = int(input())

for tc in range(1, test_case+1):
    N, M = map(int, input().split())
    board = [input() for _ in range(N)]
    answer = M * N

    check = [[0, 0, 0] for _ in range(N)]   # count - white / Blue / Red

    for idx in range(N):
        check[idx][0] = board[idx].count('W')
        check[idx][1] = board[idx].count('B')
        check[idx][2] = board[idx].count('R')
    print(check)

    a = 1
    while a < N-1:
        b = 1
        while b < N-a:
            tmp_answer = 0
            for i in range(a):        # white
                tmp_answer += check[i][1] + check[i][2]

            for j in range(a, a+b):   # Blue
                tmp_answer += check[j][0] + check[j][2]

            for k in range(a+b, N):     # Red
                tmp_answer += check[k][0] + check[k][1]

            if tmp_answer < answer:
                answer = tmp_answer

            # print(a, b)
            print(a, b, N-a-b)
            b += 1
        a += 1

    print('#{} {}'.format(tc, answer))