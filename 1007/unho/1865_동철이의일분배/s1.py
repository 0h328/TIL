import sys
sys.stdin = open('input.txt')


def permu(employee, ans):
    global answer

    if employee >= N:
        if ans > answer:
            answer = ans
        return
    elif ans <= answer:
        return
    
    
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            permu(employee+1, ans * (table[employee][i]/100))
            visited[i] = 0


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_num, max_coordinate = 0, ()
    answer = 0

    permu(0, 100)

    print('#{} {:0.6f}'.format(tc, answer))