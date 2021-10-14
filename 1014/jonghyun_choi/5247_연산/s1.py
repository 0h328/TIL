import sys
sys.stdin = open('input.txt')

# DFS 풀이는 Recursion Error가 발생할 수 밖에 없다.
def dfs(start, finish, cnt):
    global answer
    if start > 1000000:
        return

    if start == finish:
        if answer > cnt:
            answer = cnt
        return

    dfs(start + 1, finish, cnt + 1)
    dfs(start - 1, finish, cnt + 1)
    dfs(start * 2, finish, cnt + 1)
    dfs(start - 10, finish, cnt + 1)


T = int(input())

for case in range(T):
    N, M = map(int, input().split())
    answer = 987654321
    dfs(N, M, 0)

    print(answer)