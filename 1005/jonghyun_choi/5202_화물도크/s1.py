import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    N = int(input())
    work = []
    for _ in range(N):
        s, e = map(int, input().split())
        work.append((s, e))
    record = [1] * N
    sorted_work = sorted(work, key = lambda x:(x[1],x[0]))

    for i in range(N):
        temp = sorted_work[i][1]
        for j in range(i + 1, N):
            if sorted_work[j][0] >= temp:
                record[i] += 1
                temp = sorted_work[j][1]

    print('#{} {}'.format(case + 1, max(record)))