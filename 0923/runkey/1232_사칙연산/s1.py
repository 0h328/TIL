import sys
sys.stdin = open('input.txt')

def tree(node):
    if node >= V:
        return
    if V_list[node][2] > 0 :
        tree(V_list[node][2])	# 왼쪽 자식
    if V_list[node][3] > 0 :
        tree(V_list[node][3])	# 오른쪽 자식

    if V_list[node][1] == '+':
        # 왼쪽 노드와 오른쪽 노드 더하기
        V_list[node][1] = V_list[V_list[node][2]][1] + V_list[V_list[node][3]][1]
    elif V_list[node][1] == '-':
        # 왼쪽 노드와 오른쪽 노드 뺄셈
        V_list[node][1] = V_list[V_list[node][2]][1] - V_list[V_list[node][3]][1]
    elif V_list[node][1] == '*':
        # 왼쪽 노드와 오른쪽 노드 곱셈
        V_list[node][1] = V_list[V_list[node][2]][1] * V_list[V_list[node][3]][1]
    elif V_list[node][1] == '/':
        # 왼쪽 노드와 오른쪽 노드 뺄셈
        V_list[node][1] = V_list[V_list[node][2]][1] / V_list[V_list[node][3]][1]


for t in range(1, 11):
    result = ""
    V = int(input())
    V_list = [[0, 0, 0, 0] for _ in range(V + 1)]
    for i in range(V):
        n = input().split()
        if len(n) == 4:
            V_list[int(n[0])][0] = int(n[0])
            V_list[int(n[0])][1] = n[1]
            V_list[int(n[0])][2] = int(n[2])
            V_list[int(n[0])][3] = int(n[3])

        elif len(n) == 2:
            V_list[int(n[0])][0] = int(n[0])
            V_list[int(n[0])][1] = int(n[1])

    tree(1)
    result = int(V_list[1][1])
    print("#{} {}".format(t, result))