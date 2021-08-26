import sys
sys.stdin = open('input.txt')

T = int(input())


def find_min(a, b): # a = 총 숫자의 갯수 b = 총 합
    global min_value
    if a == N: # 세다가 a=N이 된건 3개를 다 픽했다는 것임으로
        if b < min_value:
            min_value = b
        return
    if b > min_value: # 이 부분이 없으면 타임에러, 중간에 넘어가면 바로 리턴
        return
    for k in range(N): # 돌면서 아직 방문하지않았다면 방문 그리고 dfs
        if check[k] == 0:
            check[k] = 1
            find_min(a + 1, b + Nums[a][k]) # 재귀에 a+1, 합
            check[k] = 0


for i in range(T):
    N = int(input())
    Nums = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N # N만큼 visit 체크
    min_value = 55555 # 1~9에서 숫라고 했으므로 임의로 숫자 지정
    find_min(0, 0)
    print('#{} {}'.format(i+1,min_value))
