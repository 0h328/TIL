import sys                                          # 눈물 겨운 하나하나 debuging 노가다의 승리 !!!
sys.stdin = open('input.txt')                       # 정답 행렬 구해놓고 답변 양식 str로 맞추는데 30분 걸림 ㅡㅡ

T = int(input())

for test_case in range(1, T+1):
    N = int(input())                                # 반복적인 내용 생략

    arr = [[0] * N for _ in range(N)]               # 해당 크기의 이차원 0행렬 생성
    cnt = 1                                         # 카운트 초기값 1
    nx = 0                                          # x축 좌표
    ny = 0                                          # y축 좌표
    dx = [1, 0, -1, 0]                              # x축 이동
    dy = [0, 1, 0, -1]                              # y축 이동
    i = 0                                           # 회전 인덱스 초기값 0

    while True:                                     # 참일때 계속 반복
        arr[ny][nx] = cnt                           # 행렬의 해당위치의 값은 cnt, 처음은 1
        if cnt == N ** 2:                           # cnt 의 값이 이차원 행렬의 총 갯수와 같을 때 종료
            break
        nx += dx[i]                                 # x축 이동
        ny += dy[i]                                 # y축 이동
        if (0 <= nx <N) and (0 <= ny < N):          # 이동한 범위가 행렬 크기 내에 있을때
            if (arr[ny][nx]) != 0:                  # 그 중에서도 값이 0이 아니면
                nx -= dx[i]                         # x축 좌표 원상복귀
                ny -= dy[i]                         # y축 좌표 원상복귀
                i = (i + 1) % 4                     # 이동 방향 변경
            else:                                   # 그 중에서도 값이 0이면
                cnt += 1                            # cnt 값 1증가
        else:                                       # 이동한 범위가 행렬 밖일 때
            nx -= dx[i]                             # x축 좌표 원상복귀
            ny -= dy[i]                             # y축 좌표 원상복귀
            i = (i+1) % 4                           # 이동 방향 변경

    # print(arr)                                    # 오우! 결과값 잘나온다.
    print('#{}'.format(test_case))                  # 귀찮은 test case 순번 표기

    for i in arr:                                   # 아니 이차원 리스트의 모든 요소를 str로 바꿔서 답변을 제출하라니 !?
        ans = ''                                    # 일일히 노가다로 답변 구현
        for j in i:
            ans += str(j) + ' '                     # 감동의 SWEA 사이트 결과 PASS
        print(ans)                                  # 의문점 : Debuging 확인 결과, 좌표 이동중에 행렬 범위를 벗어나거나 이미 숫자가 채워진 좌표에 부딪히면 좌표값을 원상복귀하고 해당 좌표에 값을 2번째 넣게됨
                                                    # 좀더 간결하게 할 수 있을 것 같은데 피곤해서 자야겠다.