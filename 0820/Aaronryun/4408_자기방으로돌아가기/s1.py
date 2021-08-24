import sys

sys.stdin = open('input.txt')

for test in range(1, 1 + int(input())):

    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    result = [0 for i in range(201)] # 지나가는 복도 길 200으로 초기화
    for i in data: # 받은 데이터를 작은 거부터 큰 값까지 탐색하도록 설정하는게 관건 + 양쪽으로 짝수 홀 수가 늘어서 있기 때문에
        if i[0] < i[1]:
            start = (i[0] + 1) // 2 # 위의 수와 아래수를 일치시키는 과정
            end = (i[1] + 1) // 2
        else:
            start = (i[1] + 1) // 2
            end = (i[0] + 1) // 2
        for j in range(start, end + 1):
            result[j] += 1
    answer = max(result)
    print('#{} {}'.format(test, answer))
