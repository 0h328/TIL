# MST(Minimum Spanning Tree) 가중치는 없음
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


# 풀이1
def dfs(i):
    global cnt
    v[i] = 1    # 출발한 곳 부터 방문 체크

    for k in tree[i]:   # 출발한 곳에서 갈 수있는 곳 확인
        if v[k] == 0:   # 방문하지 않았으면
            cnt += 1    # 방문하고 비행기 종류 개수 +1
            dfs(k)

    return cnt


T = int(input())
for _ in range(T):
    N, M = map(int, input().split()) # N: 국가의 수(노드), M: 비행기의 종류

    tree = [[] for _ in range(N+1)] # 서로 연결된 국가
    v = [0] * (N+1) # 방문 체크 필수
    cnt = 0 # 비행기 종류 개수

    for _ in range(M):
        a, b = map(int, input().split())
        tree[a].append(b)   # 1이 갈 수있는 곳은 2,3 / 2는 3
        tree[b].append(a)   # 2가 갈 수있는 곳은 1,3 / 4는 3,5

    print(dfs(1))

# 풀이2
# T = int(input())
# for _ in range(T):
#     N, M = map(int, input().split())
#     for _ in range(M):
#         input()

    # N개국 여행 / 다른 국가 이동시, 방문 국가 이동해도 가능
    # 비행기타는 횟수가 아닌, 비행기의 종류 최소 개수 a->b 랑 b->a의 비행기 종류 같음
    # print(N-1)
