def calc_min(cur_sum):
    global ans
    if ans > cur_sum:    # 최솟값 갱신
        ans = cur_sum
    return               # 명시적 종료

def dfs(k, cur_sum):
    global ans
    if ans <= cur_sum:       # 마지막 row까지 다 안봤음에도 ans 보다 크거나 같다면 이후는 유망하지 않다고 판단
        return

    # k는 증가하는 index & N은 배열의 길이(마지막 인덱스) -> k와 N이 같다는 것은 이차원 배열의 마지막 줄에 도착 했음을 의미
    if k == N:               # 만약 row 끝까지 다 살펴본 경우에 최솟값 갱신
        calc_min(cur_sum)
    for i in range(N):       # i는 column 확인
        if not visited[i]:   # 만약 현재의 row의 col에 방문하지 않았다면
            visited[i] = 1   # 방문 처리
            dfs(k+1, cur_sum + data[k][i])
            visited[i] = 0   # 원상 복구
            """
            현재의 합(cur_sum)에 현재 row(k)의 i번째 열의 값을 더한 값을 넘기며 재귀적으로 호출
            k+1 -> 다음 행(row) 체크
            data[k][i] -> 현재 보는 행/열에 해당하는 값을 cur_sum에 누적 
            """

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())        # 배열의 크기
    ans = 987654321         # 초깃값 설정
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)] # 여기서 방문 체크를 하는 것은 같은 '열'에 존재하는지 여부 판단
    dfs(0, 0)                       # dfs(k, cur_sum) / k: 인덱스 / cur_sum: 누적합
    print('#{} {}'.format(tc, ans))

"""
포인트
0 ~ N까지의 숫자에서 N개의 조합을 만들어 합이 최소가 되는 것을 찾고 
이 과정에서 불필요한 탐색을 없애보자 
"""