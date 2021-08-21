import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    corridor = [0] * 201                                        # 인덱스 연산을 복도에 맞추기 위해 200개가 아닌 201개로 설정
    for _ in range(N):
        start_room, goal_room = list(map(int, input().split())) # 출발방, 도착방
        """
        마주보는 방 == 같은 복도를 사용 -> 몫을 취하자
        """
        start_room = (start_room + 1) // 2
        goal_room = (goal_room + 1) // 2

        # 오른쪽에서 왼쪽 복귀하는 경우의 고려
        """
        예시 인풋: 오름차순(50 -> 100)
        채점 인풋: 내림차순(100 -> 50)
        """
        if start_room > goal_room:
            start_room, goal_room = goal_room, start_room
        for i in range(start_room, goal_room+1):          # 출발방 -> 도착방으로 복도 카운트
            corridor[i] += 1                              # 거치는 복도를 모두 카운트 (카운트 정렬 컨셉)

    ans = max(corridor)                                   # 가장 많이 거쳐간 복도가 최소 시간에 모든 학생들이 이동할 수 있는 시간
    print('#{} {}'.format(tc, ans))

"""
    포인트
    1. 이동 시간 -> 단위 시간
     - 1번 -> 200번 / 50번 -> 51번 이동 시간은 모두 같음
    2. 방을 이동하는 것 == 복도를 거치는 것 == 복도를 지나가는 것을 카운팅
    | 방 1   | 방 3  | 방 5  | 방 7   | 방 9    |   ...   | 방 399    |  
    | 복도 1 | 복도 2| 복도3 | 복도 4  | 복도 5  |   ...   | 복도 200 | 
    | 방 2   | 방 4  | 방 6  | 방 8   | 방 10   |   ...   | 방 400    | 
    """