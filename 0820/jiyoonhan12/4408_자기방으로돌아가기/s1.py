import sys
sys.stdin = open('input.txt')

# 아직 푸는 중
T = int(input())

for t in range(1, T+1):
    N = int(input())
    students = []
    for _ in range(N):
    # (depart, arrive) list
    # 홀수면 위 짝수면 아래... 이긴 한데 이거 필요한가?
        students.append(tuple(map(int, input().split())))
    students.sort() # test case 에서는 필요없음
    print(students)