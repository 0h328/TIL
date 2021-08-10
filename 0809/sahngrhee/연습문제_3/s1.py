import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    my_list = list(map(int, input().split()))
# N = 20
# my_list = [52, 56, 38, 77, 43, 31, 11, 87, 68, 64, 88, 76, 56, 59, 46, 57, 75, 85, 65, 53]
    new_list = []
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if my_list[j] < my_list[i]:
                cnt += 1
        new_list.append(cnt)
    my_max = new_list[0]
    for k in range(N):
        if my_max < new_list[k]:
            my_max = new_list[k]

    print('#{} {}'.format(test_case, my_max))