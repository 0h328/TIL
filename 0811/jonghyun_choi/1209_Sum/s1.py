import sys
sys.stdin = open('input.txt')

for _ in range(10):
    Case = int(input())
    num_list = [list(map(int,input().split())) for _ in range(100)]

    max_value = 0

    # 각 행의 합 중 최대값 구하기
    for i in range(len(num_list)):
        total = 0
        for j in range(len(num_list[i])):
            total += num_list[i][j]
        if total > max_value:
            max_value = total

    for j in range(len(num_list[0])):
        total = 0
        for i in range(len(num_list)):
            total += num_list[i][j]
        if total > max_value:
            max_value = total
    total1 = 0
    total2 = 0
    for i in range(len(num_list)):
        total1 += num_list[i][i]
        total2 += num_list[i][len(num_list)-1-i]
        if total1 > max_value:
            max_value = total1
        if total2 > max_value:
            max_value = total2
    print('#{} {}'.format(Case, max_value))


