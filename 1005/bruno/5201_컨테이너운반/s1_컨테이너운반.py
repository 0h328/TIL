import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    loads = sorted(list(map(int, input().split())), reverse=True)
    trucks = sorted(list(map(int, input().split())), reverse=True)
    total = 0
    # print(loads)
    # print(trucks)
    for _ in range(min(N, M)):
        if loads[0] > trucks[0]:    # 운반 불가
            loads.pop(0)            # 버리기
        else:   # 운반 가능
            total += loads.pop(0)   # 빼서 성공무게에 더하고
            trucks.pop(0)           # 사용한 트럭 제거
    print('#{} {}'.format(tc, total))

