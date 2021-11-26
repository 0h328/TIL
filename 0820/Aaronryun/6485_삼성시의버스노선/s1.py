import sys

sys.stdin = open('input.txt')

for test in range(1, 1 + int(input())):
    N = int(input())

    data = [0] * 5001 # 최대 나올 수 있는 범위의 수
    answer = []
    for i in range(N): # 범위를 받아서 받은 만큼을 범위에 플러스 해준다
        x, y = map(int, input().split())

        for j in range(x, y + 1):
            data[j] += 1

    # answer = [str(data[int(input())]) for _ in range(int(input()))]

    for _ in range(int(input())): # 해당 인덱스에 지나간 노선 수 만큼을 프린트 해준다
        answer.append(str(data[int(input())]))

    print('#{} {}'.format(test, ' '.join(answer)))