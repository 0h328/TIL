import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def Bus(K, N, M_list):
    idx = 0 #버스 위치
    charges = 0 #충전 횟수
    charges_pos = [0] * (N+1) #충전소 위치
    
    #버스충전소가 위치하면 1표시
    for m in M_list:
        charges_pos[m] += 1
        
    while True:
        #최대 이동칸만큼 우선 이동
        idx += K
        
        #현재 위치가 도착지(N)와 같거나 크면 전체 반복문 break
        if idx >= N:
            break
            
        #현재 위치에서 뒤로가며 가장 가까운 충전소 찾기
        for back_step in range(K + 1): # 0, 1, ... K
            #뒤로간 칸이 앞으로 왔던 칸과 같아졌을 때 0 return
            if back_step == K:
                return 0
            #현재 위치에 충전소가 있을 때
            if charges_pos[idx] == 1:
                charges += 1 #충전횟수 +1
                break
            #현재 위치에 충전소가 없으면 위치 1씩 뒤로 이동(idx - 1)
            idx -= 1
            
    return charges

T = int(input())

for t in range(1, T+1):
    K, N, M = map(int, input().split()) #K: 1회충전시 최대 이동칸, N: 도착지점, M: 충전소개수(사용하지 않음)
    M_list = list(map(int, input().split())) #M_list: 충전소 위치
    print('#{} {}'.format(t, Bus(K, N, M_list)))
