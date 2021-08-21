import sys
sys.stdin = open('input.txt')

def solve(num, my_list):
    node_dic = {node:[] for node in range(100)}  # 0~99까지 노드 존재

    for i in range(0, num * 2, 2):
        idx = my_list[i]                           # i = 0, 2, 4, 6, 8 ... // idx = 0, 1, 2, 3, 4 ...
        dir = my_list[i + 1]                       # i = 1, 3, 5, 7, 9 ... // idx = 0에서 출발한 노드, 1에서 출발한 노드..
        node_dic[idx].append(dir)                  # idx의 위치에 있는 node key는 idx와 동일

    visited = [0] * 100 # 0~99까지 노드에 0으로 방문하지 않았음을 표현
    initial_node = node_dic[0]  # A에서 출발이기에 0번째 노드는 1로 표현, 무조건 방문

    while initial_node:
        pop_num = initial_node.pop()

        if visited[pop_num] == 1:        # 노드에 방문한 경우
            continue
        else:                            # 노드에 방문하지 않은 경우
            next_node = []
            if pop_num in node_dic:      # 리스트에 존재하는 마지막 노드 pop의 index가 node_dic에 위치
                next_node = node_dic[pop_num]
                visited[pop_num] = 1
            if '99' in next_node:
                return 1
            initial_node.append(next_node)
    return 0

for i in range(10):
    testcase, num = map(int, input().split())
    my_list = list(map(int, input().split()))
    print('#{} {}'.format(testcase, solve(num, my_list)))