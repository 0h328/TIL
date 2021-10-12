import sys
sys.stdin = open('input.txt')

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
T = int(input())
for tc in range(1, T+1):
    cost = int(input())
    visited = [0 for _ in range(len(money))]

    for i in range(len(money)):
        while cost >= money[i]:
            cost -= money[i]
            visited[i] += 1
    print('#{}'.format(tc))
    print(*visited)

    #list 연산에서 빈 배열로 넣어주면 시간이 좀 더 오래걸림