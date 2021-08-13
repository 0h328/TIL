import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())

    my_list = [i for i in range(1, 13)]

    super_list = []
    for i in range(1, 1 << len(my_list)):
        num_list = []
        for j in range(len(my_list)):
            if i & (1 << j):
                num_list.append(my_list[j])

        super_list.append(num_list)

    cnt = 0
    for i in super_list:
        if len(i) == N and sum(i) == K:
            cnt += 1

    print('#{} {}'.format(test_case, cnt))


