# 문제 풀이 시간 : 40분
# 백트래킹 이용하는 문제였음 -> dfs 사용해야함 (다 돌면서 최소값 찾아야해서)

import sys
sys.stdin = open('input.txt')

def dfs(v):
    global cnt, result
    if cnt >= result:                    # 충전 횟수가 전의 결과 값보다 크면 더 이상 계산 안하고 빠져 나오게 하기
        return

    if v >= len(battery):                # index의 숫자가 battery 리스트의 길이보다 길어지면 빠져나오게 할건데
        result = cnt                     # cnt를 result에 넣어주고 리턴
        return                           # 아님 딱히 신경 안씀

    for i in range(v+battery[v], v, -1): # 반복문을 돌릴건데 뒤에서부터 돌릴거임, 인덱스 기준으로!
        cnt += 1                         # 왜냐면.. 어차피 가장 멀리 가기를 원하니까?
        dfs(i)                           # cnt에 1 더해주고 index 위치 변화시키기
        cnt -= 1                         # 백트래킹을 위해서 -1


T = int(input())
for tc in range(1, T+1):
    battery = list(map(int, input().split()))
    bus_station = battery.pop(0)
    result = 1000
    cnt = -1                              # 왜 답이 안나오지 100만번 고민했는데
    dfs(0)                                # 첫번째 정류장에서는 교환 횟수에서 제외 시켜야 함.. ㅜㅜ
    print('#{} {}'.format(tc, result))