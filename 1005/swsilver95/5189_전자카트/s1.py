import sys
from itertools import permutations

sys.stdin = open('input.txt', 'r')


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    idx = list(range(1, N))                             # 1. combinations를 이용해 선택하는 경우의 수를 뽑을 배열
    cases = list(permutations(idx, N - 1))              # 2. N - 1개만큼의 permutations를 이용해서 모든 경우의 수를 추출

    battery = 1001                                      # 3. 배터리 소비량은 1000을 넘을 수 없으므로 1001로 초기화
    for case in cases:                                  # 4. 모든 가능한 경우에 대해서 ex) (1, 2)
        tmp = data[0][case[0]] + data[case[N - 2]][0]   # 4.1. 처음과 끝을 이동할 때의 배터리 소비량으로 초기화 ex) 0-1 배터리 소모량 + 2-0 배터리 소모량
        for i in range(1, N - 1):                       # 4.2. 중간 부분의 배터리 소비량을 계산해서 합함
            tmp += data[case[i - 1]][case[i]]

        if battery > tmp:                               # 5. 만약 지금까지의 최소 소모량보다 적게 썼다면
            battery = tmp                               # 5.1. 갱신

    print('#{} {}'.format(tc, battery))