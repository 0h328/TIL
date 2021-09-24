import sys
sys.stdin = open('input.txt')

def solve(root):
    global cnt
    if root <= n:
        solve(root*2)                                      # 왼쪽 실행
        tree[root] = cnt
        cnt += 1
        solve(root*2 + 1)                                  # 오른쪽 실행

for tc in range(int(input())):
    n = int(input())
    tree = [0 for _ in range(n+1)]
    cnt = 1
    solve(1)                                               # 루트 부터 시작
    # print(tree)
    print('#{} {} {}'.format(tc+1, tree[1], tree[n//2]))   # 루트 저장값, n//2값

