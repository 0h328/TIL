import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    works = []
    for _ in range(N):
        start, end = map(int, input().split())
        works.append((start, end))

    for i in range(len(works)-1):
        min_idx = i
        for j in range(i+1, len(works)):
            if works[j][0] < works[min_idx][0]:
                min_idx = j
            elif works[j][0] == works[min_idx][0]:
                if works[j][1] < works[min_idx][1]:
                    min_idx = j
        works[i], works[min_idx] = works[min_idx], works[i]

    state = works[-1][0]
    cnt = 1
    while state > 0:
        for work in works[::-1]:
            if work[1] <= state:
                state = work[0]
                cnt += 1
                break
        else:
            break
    print('#{} {}'.format(test_case, cnt))