def snail(N):
    # 1. N * N 2차원 배열
    data = [[0 for _ in range(N)] for _ in range(N)]
    # 2. 0으로 초기화 된 배열에 넣을 값 (달팽이가 걸어가면서 증가 시킬 값)
    num = 1
    # 3. 가로 & 세로 값 초기화

    row = 0         # 가로
    col = -1        # 세로 (-1부터 진행하는 건 첫 가로가 N만큼 진행될 때 1을 더해 0으로 만들어 주기 위함)
    increase = 1    # index의 증감(증가 혹은 감소에 따라 -1로 부호를 변경)

    # 4. N이 0이 되기 직전까지 계속 반복
    while N > 0:
        # 4-1. 가로
        for _ in range(N):  # 리스트의 크기만큼 (어떤) 행위를 반복
            # col(가로 이동)의 값을 계속 증가
            """
            오른쪽 이동 -> increase가 양수
            왼쪽으로 이동 -> increase가 음수
            """
            col += increase
            data[row][col] = num    # 해당 위치에 num을 넣자
            num += 1                # num은 다음 이동 시에 1 증가시켜 주기 위해 +1
        N -= 1                      # 해당 반복이 끝나면 N의 크기를 1 감소시킴
        if not N:                   # 만약에 N이 0이 되면 반복 종료
            break

        # 4-2. 세로
        # 다시 N의 크기만큼 반복 (위에서 break를 만나지 않았다면 N-1이 되었을 것)
        for _ in range(N):
            # 이번에는 row(세로 이동)의 값을 계속 증가
            """
            아래로 이동 -> increase가 양수
            위로 이동 -> increase가 음수
            """
            row += increase
            data[row][col] = num    # 해당 위치에 num을 넣고 (위에서 증가된 num)
            num += 1                # 그 값은 다음 이동 시에 1 증가해야 하기 때문에 늘려주자
        # 부호 변경
        """
        ㄱ 모양에서는 모두 '증가' -> 양수
         - 왼 -> 오 이동 +  
         - 위 -> 아래 이동 + 
        ㄴ 모양에서는 모두 '감소' -> 음수
         - 오 -> 왼 이동 - 
         - 아래 -> 위 이동 -  
        """
        increase *= -1 # 방향 변경
    """
    1. 일단 한 줄씩 다 꺼내고 그걸 이어 붙이는데 -> 반복이 있을 때마다 '\n' 개행
    print([' '.join(map(str, row)) for row in data])
    ['1 2 3 4', '12 13 14 5', '11 16 15 6', '10 9 8 7']

    2. 그리고 이걸 다시 꺼내서 또 개행
    print('\n'.join([' '.join(map(str, row)) for row in data]))
    """

    snail_list = '\n'.join([' '.join(map(str, row)) for row in data])
    return snail_list

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ans = snail(N)
    print('#{}\n{}'.format(tc, ans))