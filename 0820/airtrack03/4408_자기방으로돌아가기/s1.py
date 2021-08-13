import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    corridor = [0] * 200    # 복도 길이는 방이 양 옆으로 있으므로 400 / 2

    for student in data:    # 반드시 첫번째 숫자가 두번째보다 작은 것은 아님!
        if student[0] <= student[1]:
            cor_start = (student[0]-1) // 2
            cor_end = (student[1]-1) // 2
        else:
            cor_start = (student[1] - 1) // 2
            cor_end = (student[0] - 1) // 2

        for i in range(cor_start, cor_end + 1):
            corridor[i] += 1

    print('#{} {}'.format(tc, max(corridor)))
