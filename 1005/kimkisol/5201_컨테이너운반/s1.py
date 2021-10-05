import sys

sys.stdin = open('input.txt')

'''
1. 트럭당 한 개의 컨테이너를 운반
2. 트럭의 적재용량을 초과하는 컨테이너는 운반할 수 없다.
3. A도시에서 B도시로 최대 M대의 트럭이 편도로 한번 만 운행
4. 화물의 총 중량이 최대 => 전체 무게 출력
'''
T = int(input())

#  가장 무거운거를 가장 적재용량이 적은것부터 비교해서 운반 가능할 경우 넣는 방법
for t in range(1, T + 1):
    N, M = map(int, input().split())  # N: 컨테이너 수, M : 트럭 수
    containers = sorted(list(map(int, input().split())), reverse=True)  # 컨테이너 당 무게(내림차순)
    trucks = sorted(list(map(int, input().split())))  # 트럭 당 적재 용량(오름차순)
    used = [0] * M
    max_sum = 0

    for i in range(N):
        for j in range(M):
            if used[j]:  # j번째 트럭이 이미 사용됐으면 continue
                continue
            if containers[i] <= trucks[j]:  # 컨테이너 무게가 트럭 적재 용량보다 작을 때 운반 가능
                max_sum += containers[i]  # 운반한 무게에 컨테이너 무게 추가
                used[j] = 1
                break
        if all(used):  # 만약 쓸 트럭이 없는 경우 break
            break

    print('#{} {}'.format(t, max_sum))