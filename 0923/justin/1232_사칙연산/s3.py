# 후위 순회를 활용한 풀이
# 문제에서 제시되지 않은 완전 이진 트리를 가정하고 풀이 -> 우연한 경우로 통과한 케이스

def solve(v):
    # 단말 노드가 연산자/피연산자임을 구분
    if len(tree[v]) == 2:  # 피연산자 (단말노드)
        return tree[v][1]  # 그 값을 반환

    # 이 작업이 결국 왼쪽과 오른쪽을 순회하는 것
    left = solve(tree[v][2])    # 왼쪽
    right = solve(tree[v][3])   # 오른쪽

    if tree[v][1] == '+':
        return left + right
    elif tree[v][1] == '-':
        return left - right
    elif tree[v][1] == '*':
        return left * right
    else:
        return left / right

import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    N = int(input())
    tree = [[]]                            # 비어있는 리스트를 하나 만들어 놓는 것은 첫 번째 요소의 값을 append 한 이후에 추가 된 리스트를 인덱스 1로 놓고 활용하기 위함
    for i in range(1, N + 1):              # 1번부터 N번까지 노드 번호가 순서대로 들어온다는 가정
        tree.append(list(input().split())) # 문제에서 주어지지 않은 조건이기 오답이 나올 수 있음
        if len(tree[i]) == 4:              # tree의 길이가 4인 경우? 연산자
            tree[i][2] = int(tree[i][2])   # 왼쪽 자식/오른쪽 자식을 정수로 바꿔 저장
            tree[i][3] = int(tree[i][3])
        elif len(tree[i]) == 2:            # tree의 길이가 2인 경우? 피연산자
            tree[i][1] = int(tree[i][1])   # 정수로 변경하여 저장
    ans = int(solve(1))                    # 1번부터 순회
    print('#{} {}'.format(tc, ans))