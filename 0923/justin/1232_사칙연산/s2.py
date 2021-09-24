# 후위 순회를 활용한 풀이
# 문제에서 제시되지 않은 완전 이진 트리를 가정하고 풀이 -> 우연한 경우로 통과한 케이스

def post_order(node):
    if first_child[node] == 0 or second_child[node] == 0: # 자식이 없는 경우
        return num[node]
    a = post_order(first_child[node])                 # 왼쪽 자식으로 이동
    b = post_order(second_child[node])                # 오른쪽 자식으로 이동
    num[node] = calc(operator[node], a, b)            # 계산
    return num[node]                                  # 노드에 저장된 값을 반환

def calc(op, left, right):
    if op == '+':
        result = left + right
    elif op == '-':
        result = left - right
    elif op == '*':
        result = left * right
    elif op == '/':
        result = left / right
    return result

import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    N = int(input())
    stack = []
    operator = [''] * (N+1)
    first_child = [0] * (N+1)
    second_child = [0] * (N+1)
    num = [0] * (N+1)

    for i in range(N):
        temp = list(input().split())
        idx = int(temp[0])
        if temp[1] == '+' or temp[1] == '-' or temp[1] == '*' or temp[1] == '/':
            operator[idx] = temp[1]
            first_child[idx] = int(temp[2])
            second_child[idx] = int(temp[3])
        else:
            num[idx] = int(temp[1])
    ans = post_order(1)
    print('#{} {}'.format(tc, int(ans)))