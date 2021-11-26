import sys

sys.stdin = open('input.txt')

T = int(input())
idx = 1

while idx <= T:
    N = int(input())
    input_num_list = list(map(int, input().split()))

    ans_list = []

    i = 0
    while i < N:
        # 짝수 홀수 케이스 생각
        max_idx = input_num_list.index(max(input_num_list))     # 제일 큰 거 찾아서
        ans_list.append(input_num_list.pop(max_idx))            # 넣고
        min_idx = input_num_list.index(min(input_num_list))     # 제일 작은 거 찾아서
        ans_list.append(input_num_list.pop(min_idx))            # 넣고

        i += 1

    ans = ' '.join(map(str, ans_list))

    print('#{0} {1}'.format(idx, ans))

    idx += 1
