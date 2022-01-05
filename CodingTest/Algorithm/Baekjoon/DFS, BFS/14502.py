from collections import deque
import sys
sys.stdin = open('input.txt')

def wall(cnt):

    if cnt == 0:                            # 벽을 모두 세운경우
        virus()                             # 바이러스 퍼짐 조사
        return

    for i in range(N):                      # 벽세우기 완전 탐색
        for j in range(M):
            if wall_arr[i][j] == 0:         # 안전 영역이면
                wall_arr[i][j] = 1          # 벽세우고
                wall(cnt-1)                 # 벽 개수 -1
                wall_arr[i][j] = 0          # 탐색 후 다시 벽 없애고, 다른 곳 세우기

def virus():

    global max_zone
    virus_arr = [w[:] for w in wall_arr]    # 바이러스 퍼지는 배열을 체크하기 위해 copy (속도: slice > deepcopy)
                                            # copy안하면 바이러스가 퍼진 채 탐색을 하게 되므로 copy
    q = deque()
    for i in range(N):
        for j in range(M):                  # 완전 탐색
            if virus_arr[i][j] == 2:        # 바이러스 있는 곳 찾고
                q.append((i, j))            # 큐에 저장

    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    while q:
        r, c = q.popleft()                  # 바이러스 좌표 pop
        for i in range(4):                  # 4방으로 바이러스 퍼뜨리기
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M and virus_arr[nr][nc] == 0:  # 배열 범위 & 안전영역인 경우
                q.append((nr, nc))
                virus_arr[nr][nc] = 2       # 바이러스 퍼짐

    safety_zone = 0                         # 바이러스가 모두 퍼지고 안전영역 개수 찾기
    for i in range(N):
        for j in range(M):
            if virus_arr[i][j] == 0:
                safety_zone += 1

    if max_zone < safety_zone:              # 안전영역 개수와 최대 안전영역을 비교하면서 갱신
        max_zone = safety_zone

N, M = map(int, input().split())
wall_arr = [list(map(int, input().split())) for _ in range(N)]  # 전체 배열에 벽을 세워서 안전영역을 체크하기 위한 리스트
max_zone = 0

# 벽은 꼭 3개를 세워야 하므로
wall(3)
print(max_zone)

# 리스트 복사 방식 (deepcopy vs slicing)
# deepcopy
# 모듈은 객체의 모든 속성과 데이터를 복사해온다.
# 때문에 배열보다는 class객체나, dictionary같은 해쉬값을 복사해올때 이점이 있을 것.
# 또한 코드를 뜯어보면 memo 속성을 넣을 수 있는데, 최적화하는데 사용할 수 있다고 한다.
# 모듈 import에 꽤 긴 시간이 소요될 수 있다.

# slicing
# slicing은 리스트의 요소 갯수만큼의 시간 복잡도를 가짐
# copy모듈 안에서 여러 연산을 수행하는 것 보다 시간이 적게 소요될 수 있음.

# 결론
# 배열의 깊은 복사를 하기 위해서는 slicing을 이용하는 것이 좋음.

# <출처 : https://velog.io/@emplam27/파이썬-리스트의-깊은복사는-deepcopy가-빠를까-slicing이-빠를까>

