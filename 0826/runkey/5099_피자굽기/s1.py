import sys
sys.stdin = open('input.txt')

'''
5 9 3 9 9 2 5 8 7 1
2 4 1 4 4 2 5 8 7 1
1 2 0 2 2 2 5 8 7 1
0 1 0 1 1 1 5 8 7 1
0 0 0 0 0 0 2 8 7 1
0 0 0 0 0 0 1 4 3 0
0 0 0 0 0 0 0 2 1 0
0 0 0 0 0 0 0 1 0 0
'''

t = int(input())                                # 테스트 케이스 갯수
for tc in range(1, t + 1):                      # 테스트 케이스 갯수
    N, M = map(int, input().split())            # N, M에 화덕 크기와 피자 갯수를 넣음
    C = list(map(int, input().split()))         # C에 M개의 피자에 들어가는 치즈 양을 넣어줌
    fire_pit = [0] * N                          # 화덕에 피자가 있는지 확인
    result = 0                                  # 결과가 담길 최종 인덱스
    fire_idx = 0                                # 화덕의 인덱스
    c_idx = 0                                   # 피자의 인덱스

    while C.count(0) != M:                      # 치즈의 0의 갯수가 피자갯수랑 같아질 때까지 진행
        if fire_idx == N - 1:                   # fire_idx가 화덕의 크기와 같으면 화덕이 한 바퀴 회전한 것이므로
            fire_pit[fire_idx] //= 2            # 해당 화로 자리를 2로 나눔
            if fire_pit[fire_idx] == 0:
                fire_idx = 0                    # fire_idx를 0으로 초기화
                C[c_idx] = fire_pit[fire_idx]   # 치즈 양을 반으로 줄여줌
                c_idx += 1
                fire_pit[fire_idx] = C[c_idx]

            if C.count(0) == M - 1:
                result = c_idx

        else:                                               # 화덕에 자리가 남아 있으면
            fire_pit[fire_idx] = C[c_idx]
            fire_idx += 1
            c_idx += 1

    print("#{} {}".format(tc, result))  # 출력