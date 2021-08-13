import sys
sys.stdin = open('input.txt')

def ladder(arr):
    start = [i for i in range(1, 101) if arr[1][i] == 1]    # 시작 좌표 찾기(x=1일때 => 테두리 고려)

    for y in start:                                         # y값으로 받음
        solution = y                                        # 결과로 출력할 수 있으므로 저장
        x = 1                                               # x좌표
        visited = set([(x, y)])                             # 방문한 지역 더 방문 안하도록 만듬
        while x < 100:                                      # x가 100이 되면 종료
            if arr[x][y+1] and (x, y+1) not in visited:     # 오른쪽으로 이동 가능하고, 방문한 적 없는 경우
                visited.add((x, y+1))                       # 방문 표시
                y += 1
            elif arr[x][y-1] and (x, y-1) not in visited:   # 왼쪽으로 이동 가능하고, 방문한 적 없는 경우
                visited.add((x, y-1))
                y -= 1
            else:                                           # 아래쪽으로 이동
                visited.add((x+1, y))
                x += 1

        if arr[x][y] == 2:                                  # while문이 끝난 좌표(x=100)가 2인 경우
            return solution - 1                             # 결과값 반환(테두리 제외하고(-1) 출력)

for _ in range(10):
    N = int(input())
    arr = [[0] * 102] + [[0] + list(map(int, input().split())) + [0] for _ in range(100)] + [[0] * 102] # 테두리 0으로 생성
    print('#{} {}'.format(N, ladder(arr)))