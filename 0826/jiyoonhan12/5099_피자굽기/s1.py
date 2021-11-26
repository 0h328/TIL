import sys
sys.stdin = open('input.txt')

def pizza():
    pit = []
    for i in range(N): # N개의 피자 추가
        pit.append([Ci[i], i])
    # print(pit)

    p = 0
    while len(pit) != 1: # 화덕에 피자 1개 남을 때까지
        pit[0][0] = pit[0][0] // 2 # 화덕 첫 번째 피자의 치즈를 반으로 줄임
        if pit[0][0] == 0: # 치즈 0
            if N + p < M: # M에 아직 화덕에 안 들어온 피자 있다면
                pit.pop(0)
                pit.append([Ci[N+p], N+p])
                p += 1
            else: # 남은 피자 없다면
                pit.pop(0)
        else: # 치즈 0 아니면 pop-append
            pit.append(pit.pop(0))

    return pit[0][1] + 1 # 첫 인덱스 0으로 잡았었기 때문에 +1


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    Ci = list(map(int, input().split()))
    res = pizza()
    print('#{} {}'.format(t, res))