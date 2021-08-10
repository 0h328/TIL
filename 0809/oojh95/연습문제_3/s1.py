import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    first_state = list(map(int, input().split()))

    max_fall = 0
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if first_state[j] >= first_state[i]:    # 낙차를 구하기 위해 기준값보다 블록의 갯수가 큰 것이 몇개 있는지 확인
                cnt += 1
        cnt = N - i - 1 - cnt   # 전체 길이에서 i만큼 뺀것이 state[i]의 낙차이며 사이 공간이므로 -1을하고 i위치이후 i보다 더 많은 불록갯수를 가진 cnt를 빼면 총 낙차거리가나옴
        if cnt > max_fall:
            max_fall = cnt  #최대낙차를 구하기 위한 비교
    print('#{} {}'.format(test_case, max_fall))
