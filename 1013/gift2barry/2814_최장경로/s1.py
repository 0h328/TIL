import sys
sys.stdin = open('input.txt')

'''
미해결 너무 피곤 내일 마저 하자
풀이 8분
thought process: 2분
재귀 돌면서 스택 안에 방문했던 원소를 넣어, 같은 원소를 방문하려하면 바로 stop
append 와 pop 활용
이와 같이 중복 방문 미연에 방지
'''

def dfs(v, cnt):
    global ans

    if cnt > ans:
        ans = cnt
    if not visited[v]:
        visited[v] = 1
        for k in range(1, N+1):
            if G[v][k] == 1:
                dfs(k, cnt + 1)
    else:
        return


for tc in range(1, int(input())+1):

    N, M = map(int, input().split())
    ans = 0
    if M > 0:
        G = [[0] * (N + 1) for _ in range(N + 1)]
        visited = [0] * (N + 1)
        for i in range(M):                              # 인접리스트 생성
            x, y = map(int, input().split())
            G[x][y] = 1
            G[y][x] = 1

        dfs(1, 1)      # 탐색시작 노드 1, 카운트



'''
손절2
실패
총 풀이시간 12분
thought process: 1분
visited 1차원배열 생성, 입력 노드 정보 받아와서
노드=인덱스위치 라 생각해서 visited 1 로 채움
연속적으로 이동 가능하면 계속 cnt 누적하다가, 안되면 초기화해서 다시 누적
'''

'''
N개의 정점과 M개의 간선으로 구성된 가중치가 없는 무방향 그래프에서의 최장 경로의 길이를 계산.

정점의 번호는 1번부터 N번까지 순서대로 부여되어 있다.

경로에는 같은 정점의 번호가 2번 이상 등장할 수 없으며, 경로 상의 인접한 점들 사이에는 반드시 두 정점을 연결하는 간선이 존재해야 한다.

경로의 길이는 경로 상에 등장하는 정점의 개수를 나타낸다.
'''

# for tc in range(1, int(input())+1):
#
#     N, M = map(int, input().split())
#     ans = 1
#
#     if M > 0:
#
#         nums = tuple(tuple(map(int, input().split())) for _ in range(M))
#         visited = [0] * (M + 2)
#
#         for i in range(M):
#             visited[nums[i][0]] += 1
#             visited[nums[i][1]] += 1
#
#         tmp = 0
#         for j in visited:
#             if j == 1:
#                 tmp += 1
#                 if tmp > ans:
#                     ans = tmp
#             else:
#                 tmp = 0
#
#     print('#{} {}'.format(tc, ans))


'''
손절1
미해결 49분 
thought process: 15분
간선이 1개 이상일때 코드 실행
일단 인접리스트 생성
시작 간선위치는 항상 1
정점의 번호는 N 까지
재귀 활용

cnt 값 ans 와 비교해서 최대값 갱신

'''

# def dfs(v, cnt):
#
#     visited[v] = cnt
#
#     if 0 not in visited[1:]:
#         return max(visited)
#
#     if my_list[v]:
#         new_v = my_list[v]
#         dfs(new_v, cnt + 1)
#
#
# for tc in range(1, int(input())+1):
#
#     N, M = map(int, input().split())
#     if M > 0:
#         my_list = [0] * (M + 1)
#         nums = tuple(tuple(map(int, input().split())) for _ in range(M))
#         visited = [0] * (M + 1)
#
#         for i in range(M):                              # 인접리스트 생성
#             my_list[nums[i][0]] = nums[i][1]
#
#         dfs(1, 1)      # 탐색시작 노드 1, 카운트