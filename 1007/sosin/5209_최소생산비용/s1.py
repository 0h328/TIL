import pathlib, sys
sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + '/input.txt')

def find_sol(r, ans, selected):
    global result
    if r == N:
        result = ans
        return

    for k in range(N):
        if k not in selected and result > ans+matrix[r][k]:
            find_sol(r+1, ans+matrix[r][k], selected+[k])
    return

for T in range(int(input())):
    result = 1e9
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    for i, t in enumerate(matrix[0]):
        find_sol(1, t, [i])

    print('#{} {}'.format((T+1), result))


#1 63
#2 78
#3 129