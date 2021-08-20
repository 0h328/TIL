import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    print('#{}'.format(tc))     # 출력 방식 유의
    N = int(input())
    tmp = []
    print(1)                    # 1 먼저 출력
    for i in range(N-1):        # N-1번 출력 -> 가장 마지막 값은 밑에서 append
        result = [1]            # 항상 처음은 1이 필요
        for j in range(i):      # 가운데서 필요한 값을 위해 i만큼 반복
            result.append(tmp[j] + tmp[j+1])    # 값을 하나씩 더해가자
        result.append(1)                        # 항상 마지막은 1
        print(*result)
        tmp = result                            # tmp 에서 하나씩 값을 더해가기 때문에 tmp를 result로 갱신