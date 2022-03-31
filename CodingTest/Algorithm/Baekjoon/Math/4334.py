import sys
sys.stdin = open('input.txt')

C = int(input())
for _ in range(C):
    students = list(map(int, input().split()))

    cnt = 0
    for i in range(1, students[0]+1):
        if students[i] > sum(students[1:]) / students[0]:
            cnt += 1

    avg = cnt / students[0] * 100
    print(f'{avg:.3f}%')