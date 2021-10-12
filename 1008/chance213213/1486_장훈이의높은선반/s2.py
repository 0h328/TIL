import sys
sys.stdin = open('input.txt')

def tower(people, height):
    global ans
    if height >= ans:
        return
    if people == N:
        if height >= B and ans > height:
            ans = height
        return

    tower(people + 1, height)
    tower(people + 1, height + H[people])


T = int(input())

for case in range(T):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    visited = [0 for _ in range(N)]
    print(visited)
    ans = 987654321
    tower(0, 0)
    print('#{} {}'.format(case + 1, ans - B))