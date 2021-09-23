import sys
sys.stdin = open('input.txt')

# 디버깅 2시간 반
# 풀이시간 2시간
# thought process: 15분
# leaf 노드 위치에서 시작해서 // 2 로 부모 노드의 연산자 확인 후
# 두 자식노드 연산하고 해당 부모 노드에 덮어쓰기 반복
# 루트노드인 tree[1] 반환

def calc(n):
    if temp[n][1] == '*':
        ans = tree[int(temp[n][2])] * tree[int(temp[n][3])]
    elif temp[n][1] == '/':
        ans = tree[int(temp[n][2])] // tree[int(temp[n][3])]
    elif temp[n][1] == '-':
        ans = tree[int(temp[n][2])] - tree[int(temp[n][3])]
    elif temp[n][1] == '+':
        ans = tree[int(temp[n][2])] + tree[int(temp[n][3])]
    return ans

for tc in range(1, 10+1):
    N = int(input())
    temp = [[0]] + list(input().split() for _ in range(N))
    tree = [0] * (N+1)
    i = N
    while i > 0:
        if temp[i][1].isnumeric():
            tree[i] = int(temp[i][1])
        else:
            tree[i] = calc(i)
        i -= 1
    print('#{} {}'.format(tc, tree[1]))