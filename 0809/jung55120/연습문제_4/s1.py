import sys
sys.stdin = open('input.txt')

def baby_gin(arr):
    result = 0
    counting = [0] * 10

    for i in arr:
        counting[i] += 1

    cnt = 0
    while cnt < 10:
        if counting[cnt] >= 3:
            counting[cnt] -= 3
            result += 1
            continue

        if counting[cnt] >= 1 and counting[cnt+1] >= 1 and counting[cnt+2] >= 1:
            counting[cnt] -= 1
            counting[cnt + 1] -= 1
            counting[cnt + 2] -= 1
            result += 1
            continue

        cnt += 1
    return 1 if result == 2 else 0

T = int(input())

for tc in range(T):
    arr = list(map(int, input()))
    print(baby_gin(arr))