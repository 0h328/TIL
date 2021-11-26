import sys
sys.stdin = open('input.txt')

def subSet():
    result = []
    for i in range(1<<len(arr)):                    # 비트 마스킹
        temp = []                                   # 안쪽 for문이 실행된 값을 저장할 공간
        for j in range(len(arr)):
            if i & (1<<j):
                temp.append(arr[j])
            if len(temp) > N or sum(temp) > K:      # N보다 요소가 많아지고, 합 값이 커지면 추가 연산할 필요 없음
                break
        else:
            if len(temp) == N and sum(temp) == K:   # 지정한 요소의 수와 합 값인 경우
                result.append(temp)                 # result에 추가
    return len(result)

T = int(input())
arr = list(range(1, 13))
for test in range(T):
    N, K = map(int, input().split())
    print('#{} {}'.format(test+1, subSet()))