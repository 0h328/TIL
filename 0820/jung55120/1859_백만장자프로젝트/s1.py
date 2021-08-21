import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    num = int(input())
    cost = list(map(int, input().split()))

    stack = []
    max_cost = 0
    result = 0
    for i in range(1, len(cost)):
        if cost[i] >= cost[i-1]:
            stack.append(cost[i-1])
        elif cost[i] < cost[i-1]:
            max_cost = cost[i-1]
            money = (max_cost * len(stack)) - sum(stack)




    print(money)


    # print('#{} {}'.format(tc, result))