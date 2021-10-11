import sys

sys.stdin = open('input.txt')
"""
dp를 이용해서 푼다 디피는 탈영병을 잡는게 아니라 동적계획법이다... 그건 이전의 값을 활용하는거고 시간적 효율성이 올라간다.
만약 수열을 다 구한다면? 경우의 수는 N!이니깐 시간이 O(N!)...딱봐도 별로다

"""
def assign(N, cost): # (k,mask)활용 k-1까지 할당된 사람의 수 , mask j 번째 비트를 통해 j 번째 작업이 할당되었는지 확인
    dp = [0] * (1 << N)
    dp[0] = 1
    for mask in range(1 << N): # 모든 경우의 수 마스크
        x = bin(mask).count('1') # 현재까지 조합의 가짓수 즉, 선택해야 하는 행의 번호
        for j in range(N): # 분배할 수 있는 작업의 순서
            if not mask & (1 << j): # 만약 아무에게도 배정받지 않은 작업이라면? 배정한다.
                print((x,j) , mask|(1<<j), mask)
                dp[mask | (1 << j)] = max(dp[mask | (1 << j)], dp[mask] * cost[x][j]) # j번째 작업을 할당할 때 k번 쨰의 사람이 처리하기 위한 최소의 비용
                # k는 다음 단계가 k+1  , mask 는 다음 단계가 mask|(1<<j) 즉, 새로 확인할 위치의 비용과 이전까지 곱한 비용을 비교해서 더 작은 값을 현재값에 저장해준다.

    print(dp)
    return dp[- 1]


for test in range(1, 1 + int(input())):
    N = int(input())
    data = [list(map(lambda x: x / 100, map(int, input().split()))) for _ in range(N)]

    answer = assign(N, data)*100

    print('#{} {:.6f}'.format(test,answer))