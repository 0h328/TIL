import sys
sys.stdin = open('input.txt')


'''
총 소요시간 49분
thought process: 7분 
문제 이해 잘 안가서 해답코드 보고 이해하고 코드 작성

원소 * 원소 * 0.01 해서 최대값 탐색, 고로 갱신형으로 구현

DP 활용해보고 싶지만,, 세번째 조건을 못 찾아서 포기
DP의 조건: 
1. 메인 problem 이 sub problems 로 쪼개진다
2. sub problems 의 solution 으로 상위 problem 의 solution 을 구할 수 있다
3. sub problem 들이 겹친다 (피보나치와 비슷해서, memorization 활용하는 구간)

고로, dfs 활용, visited도 활용

어차피 최대 확률을 찾는거니까, 모든 사람들이 일을 해야 확률 올라감 == 모든 인덱스 순회해야 최대값에 가까워짐
고로, 
'''

def dfs(idx, p):
    global ans
    if idx == N:
        if p > ans:
            ans = p
            return

    if p <= ans:        # 이 부분은 < 로 하면 'badgateway' 왜지;
        return

    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                next_p = p * arr[idx][i] * 0.01     # 확률 계산
                dfs(idx+1, next_p)                  #
                visited[i] = 0
    return

for tc in range(1, int(input())+1):

    N = int(input())
    arr = tuple(tuple(map(int, input().split())) for _ in range(N))
    visited = [0] * N                   # 행 기준으로 한줄씩 차지, 고로 1차원 visited 충분
    ans = -1
    dfs(0, 1)                           # 위치 인덱스, 최초 확률값 구하기위한 값
    print('#{} {}'.format(tc, format(ans*100, '.6f')))
