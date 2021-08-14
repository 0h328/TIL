import sys

sys.stdin = open('input.txt', encoding='UTF-8')

T = int(input())

test_case = 1
while test_case <= T:

    N = int(input())
    num_list = list(map(int, input().split()))

    # min_num = num_list[0]
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if num_list[minIdx] > num_list[j]:
                minIdx = j
        num_list[i], num_list[minIdx] = num_list[minIdx], num_list[i]

    # print(num_list)
    print('#{}'.format(test_case), end = ' ')
    for e in num_list:
        print(e, end = ' ')
    print()
    # break
    test_case += 1