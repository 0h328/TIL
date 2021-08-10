import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())                          # 정사각형 크기
    blocks = list(map(int, input().split()))  # 상자의 길이가 담겨있는 배열
    max_drop = 0                              # 낙차가 가장 큰 값 구하기

    for cur in range(N-1):             # N-1? 마지막에 있는 요소는 벽에 붙어있기 때문에 비교 불가
        cur_block = blocks[cur]        # 현재 블럭
        parts = blocks[cur+1:]         # parts => current 다음에 있는 나머지 요소 블럭(리스트)
        drop = 0                       # 낙차 크기 기록 -> cur_block blocks의 요소 간의 비교를 통해 낙차를 구해가자!
        for idx in range(len(parts)):  # 비교 대상의 리스트 크기만큼 반복을 돌면서
            if cur_block > parts[idx]: # 현재보다 낮은 상자의 개수를 카운트 (이때 낙차로 기록되지 않고 상자가 쌓이기 때문에 같아도 안됨)
                drop += 1              # 낙차의 개수를 1 증가 시키자

        if max_drop < drop:           # 최종 낙차의 크기가 구해지면 기존의 낙차크기와 비교하여 낙차의 최댓값 갱신
            max_drop = drop
    print('#{} {}'.format(tc, max_drop))