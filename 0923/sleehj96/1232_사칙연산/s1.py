import sys
sys.stdin = open('input.txt')

def calculate(node):

    val = G[node]
    if val == '+':
        return calculate(childs[node][0]) + calculate(childs[node][1])
    elif val == '-':
        return calculate(childs[node][0]) - calculate(childs[node][1])
    elif val == '*':
        return calculate(childs[node][0]) * calculate(childs[node][1])
    elif val == '/':
        return calculate(childs[node][0]) // calculate(childs[node][1])
    else:
        return val


for tc in range(10):
    N = int(input())
    G = [0]
    childs = [[] for _ in range(N+1)]

    for _ in range(N):
        input_list = list(input().split())
        input_len = len(input_list)

        idx = int(input_list[0])

        if input_len == 2:
            val = int(input_list[1])
        else:
            val = input_list[1]
            left_idx = int(input_list[2])
            right_idx = int(input_list[3])
            childs[idx].append(left_idx)
            childs[idx].append(right_idx)

        G.append(val)

    # print(G)
    # print(childs)
    root = 1
    ans = calculate(root)
    #
    #     nums = list(map(int, input().split()))
    #
    #     for idx, num in enumerate(nums):
    #         put_tree(idx+1, num)
    #
    #     # print(G)

    print('#{0} {1}'.format(tc+1, ans))
    # break
