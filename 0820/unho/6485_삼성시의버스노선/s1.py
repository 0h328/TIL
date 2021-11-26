'''
문제 해법보다 문제를 읽는데 더 오래걸림...

예상 연산횟수에 따른 풀이

1. 5,000 크기의 리스트를 0으로 초기화
2. 노선이 지나는 경우 각 인덱스의 값 + 1
3. 각 정류장은 몇개의 노선이 지나가는지 반환
최악의 경우 - 500(N) * 5,000(A1,B1) * 500(P) -> 1,250,000,000

1. 모든 값을 입력받음
2. C1 의 정류소 번호가 나오면 A1 B1 범위가 몇개 속하는지 카운트
최악의 경우 - 500(P) * 500(N) -> 250,000
'''


import sys
sys.stdin = open('input.txt')


test_case = int(input())


for tc in range(1, test_case+1):
    n = int(input())                                                    # 노선 수
    n_list = [list(map(int, input().split())) for _ in range(n)]        # 노선의 출발점과 도착점을 2차원 배열로 할당

    p = int(input())                                                    # 확인할 버스정류장 수
    answer = []                                                         # 정답 변수

    for _ in range(p):                                                  # 확인할 버스정류장 수만큼 반복
        c = int(input())                                                # 확인할 버스 정류장 번호
        cnt = 0                                                         # 몇개 버스가 지나는지 카운트

        for e in n_list:                                                # 모든 노선 반복하여 확인
            if e[0] <= c <= e[1]:                                       # 확인할 버스 정류장 번호가 출발점과 도착점 사이에 있으면
                cnt += 1

        answer.append(cnt)

    print('#{}'.format(tc), end=' ')
    print(*answer)