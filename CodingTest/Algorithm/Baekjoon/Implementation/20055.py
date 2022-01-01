# deque의 rotate 이용
from collections import deque
import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())    # N: 길이, K: 내구도
belt = deque(list(map(int, sys.stdin.readline().split())))   # belt 각 칸(idx)의 내구도
step = 1    # 가장 처음 수행되는 단계가 1번째 단계이므로 1

robot = deque([0] * N)  # [0, 0, 0] # robot과 belt 윗면의 길이를 같게 함 (len(robot) = N)

while True:

    # 1. belt가 각 칸 위에 있는 robot과 함께 한 칸 회전한다.
    belt.rotate(1)  # belt 오른쪽 회전
    robot.rotate(1) # robot 오른쪽 회전
    robot[-1] = 0   # 회전할때 robot의 마지막 idx는 내리므로, 0


    # 2. 먼저 올라간 robot부터 belt가 회전하는 방향으로 한 칸 이동하고, 이동을 못하면 가만히 있는다.
    for i in range(N-2, -1, -1):    # 가장 먼저 올라간 robot이 rotate까지 거쳤으면 뒤 idx 쪽에 있으므로 내리기 전 칸부터 탐색
        if robot[i] and robot[i+1] == 0 and belt[i+1]:  # 내구도가 있고, 현재 위치에 robot있어야하고, 다음 위치에 robot 없어야함
            belt[i+1] -= 1      # robot이 이동했으므로 내구도 -1
            robot[i+1] += 1     # 다음위치로 robot이 이동했으므로, 다음 위치 idx에 robot +1
            robot[i] -= 1       # 현재위치의 robot이 다음으로 이동 했으므로, 현재 위치 idx에 robot -1
            # robot.rotate(1)   # 안되는 이유????
    robot[-1] = 0   # 내리는 위치까지 갔으면, robot -1 (내려야함)


    # 3. 올리는 위치(belt[0])에 내구도가 0이 아니면 올리는 위치에 robot을 올림.
    if belt[0] and robot[0] == 0:
        robot[0] += 1   # belt 위치와 robot위치가 같으므로 belt 위치에 올라갔으면 robot +1
        belt[0] -= 1    # belt 내구도는 robot을 올렸으므로 -1


    # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 종료
    if belt.count(0) >= K:
        break

    step += 1   # 4.에 충족되지 않으면 단계 반복 (+1)

print(step)