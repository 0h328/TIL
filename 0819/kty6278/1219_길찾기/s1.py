import sys
sys.stdin = open('input.txt')

def solve(num, my_list):
    node_dic = [[] for _ in range(100)]  # 0~99까지 노드 존재
    for i in range(0, num * 2, 2):
        node_dic[my_list[i]].append(my_list[i + 1])                  # idx의 위치에 있는 node key는 idx와 동일


    visited = [0] * 100  # 0~99까지 노드에 0으로 방문하지 않았음을 표현
    result = 0

    stack = [0]
    while len(stack) > 0:
        curr = stack.pop()

        # 종료 조건
        if curr == 99:
            result = 1
            break
        # 방문했던 노드인 경우
        else:
            if visited[curr]:
                continue
        # 방문하지 않았던 노드인 경우 stack에 push
        for j in node_dic[curr]:
            if visited[j] != 1:
                stack.append(j)
    return result



for i in range(10):
    testcase, num = map(int, input().split())
    my_list = list(map(int, input().split()))
    print('#{} {}'.format(testcase, solve(num, my_list)))