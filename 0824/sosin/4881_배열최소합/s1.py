import sys

sys.stdin = open('input.txt')

from itertools import permutations

def sol(sel, i, selected, sum_result):
    global result
    if result < sum_result:
        return
    if i == N:
        result = min(result, sum_result)
        print(sel)
    else:
        for j in range(N):
            if j not in selected:
                sel[i][j] = 1
                sum_result+=arr[i][j]
                selected.append(j)
                sol(sel, i+1, selected, sum_result)
                selected.pop()
                sum_result-=arr[i][j]
                sel[i][j] = 0

for T in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sel = [[0]*N for _ in range(N)]

    result = 1e9
    sol(sel, 0, [], 0)

    print('#{} {}'.format((T+1), result))

#1 8
#2 14
#3 9
