# 동완님 풀이
import sys
sys.stdin = open('input.txt')

def charging(arr, K, N, M):
    state = result = 0 # state: 현재 칸 // result: 충전한 횟수

    while state < N:
        if N - state <= K: # 충전 없이 이동할 수 있는 경우
            break # 충전 안하고 도착하므로 그대로 while문 벗어남

        for i in range(K, 0, -1): # K ~ 1까지(0은 포함하면 안됨)
            if (state+i) in arr: # state+이동칸의 값이 arr(충전소)에 있는 경우
                state += i # 이동
                result += 1 # 충천 횟수 +1
                break # 더 이상 돌 필요 없음(+갈 곳 없는 경우 else문 실행시켜야 함)
        else: # 더 이상 충전하고 못 가는 경우
            return 0 # 0 반환
    return result # 결과 반환

T = int(input())

for i in range(T):
    K, N, M = map(int, input().split())
    arr = set(map(int, input().split()))
    print('#{} {}'.format(i + 1, charging(arr, K, N, M)))