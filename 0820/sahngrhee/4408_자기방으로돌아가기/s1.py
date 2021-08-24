import sys
sys.stdin = open('input.txt')

def div(num):
    return (int(num)+1) // 2


T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 돌아갈 사람의 수

    students = [list(map(div, input().split())) for _ in range(N)]
    print(students)

    road = [0] * 201

    for i in range(N):
        if students[i][0] > students[i][1]:
            students[i][0], students[i][1] = students[i][1], students[i][0]

        for j in range(students[i][0], students[i][1]+1):
            road[j] += 1

    print('#{} {}'.format(test_case, max(road)))