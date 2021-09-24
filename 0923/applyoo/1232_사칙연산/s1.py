import sys
sys.stdin = open('input.txt')


def cal(x, y, c):  # 계산 함수
    if c == '+': return x + y
    elif c == '-': return x - y
    elif c == '*': return x * y
    else: return x / y


def post_order(node):  # 후위 순회
    global ans
    if node:
        post_order(tree[node][1])
        post_order(tree[node][2])
        ans.append(tree[node][0])


for tc in range(1, 11):
    N = int(input())
    tree = [[0] * 3 for _ in range(N+1)]  # 인덱스(0~2): 노드 값, 왼쪽 인덱스, 오른쪽 인덱스

    for i in range(1, N+1):
        t = input().split()
        if len(t) > 2:  # 노드 값이 연산자인 경우
            tree[i] = t[1], int(t[2]), int(t[3])
        else:  # 노드 값이 숫자인 경우
            tree[i][0] = int(t[1])

    ans = []
    post_order(1)  # 루트 노드는 1로 고정되어 있음

    q = []
    for v in ans:
        if v not in ('+', '-', '*', '/'):  # 연산자가 아니면 그냥 push
            q.append(v)
        else:  # 연산자면 pop을 2번 하여 연산 후 다시 push
            a = q.pop()
            b = q.pop()
            q.append(cal(b, a, v))  # 연산 순서 주의해야 함

    print('#{0} {1}'.format(tc, int(q[0])))
