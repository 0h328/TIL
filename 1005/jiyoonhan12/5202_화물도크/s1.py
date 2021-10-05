import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    timetable = []
    for _ in range(N):
        timetable.append(tuple((map(int, input().split()))))
    timetable.sort(key=lambda x:x[1])
    # print(timetable)
    cnt = 0
    last = 0 # 이전 작업 끝난 시간
    while timetable:
        s, e = timetable.pop(0)
        if s >= last:
            cnt += 1
            last = e

    print('#{} {}'.format(t, cnt))