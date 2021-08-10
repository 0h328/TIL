import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def Bus(K, N, M):
    idx = 0
    charges = 0
    cnt_charge = [0] * (N+1)
    #버스충전기 위치
    for m in M:
        cnt_charge[m] += 1
    while True:
        #최대 이동칸
        idx += K
        #현재 위치가 도착지(N)와 같거나 크면 전체 반복문 break
        if idx >= N:
            break
        for back_step in range(K + 1):
            #뒤로간 칸이 1회 충전시 최대 이동칸과 같아졌을 때 0 return
            if back_step == K:
                return 0
            #현재 위치에 충전기가 있을 때
            if cnt_charge[idx] == 1:
                charges += 1 #충전횟수 +1
                break
            #현재 위치에 충전기가 없으면 위치 1씩 뒤로 이동(idx - 1)
            idx -= 1
    return charges

T = int(input())

for t in range(1, T+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))
    print('#{} {}'.format(t, Bus(K, N, charge)))
