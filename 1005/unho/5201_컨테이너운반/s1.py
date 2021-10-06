import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    container = sorted(list(map(int, input().split())))     # 정렬
    truck = sorted(list(map(int, input().split())))         # 정렬
    answer = 0

    while container and truck:              # 두개다 남아있을때까지
        if truck[-1] >= container[-1]:      # 트럭이 옮길수있으면
            answer += container[-1]
            truck.pop()                     # 트럭 사용
        container.pop()                     # 컨테이너 운반 가능 여부 학인 끝

    print('#{} {}'.format(tc, answer))    