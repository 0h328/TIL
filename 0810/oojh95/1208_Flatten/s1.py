import sys
sys.stdin = open('input.txt')

T = 10  #테스트케이스
for test_case in range(1, T + 1):
    dump = int(input()) #덤프횟수
    height_state = list(map(int, input().split()))  #초기 높이 정보(가로는 100)

    for i in range(dump):   # 문제에서 제시한대로 최대값과 최소값을 덤프 숫자만큼 옮기는 작동을 해줌
        height_state[height_state.index(max(height_state))] -= 1
        height_state[height_state.index(min(height_state))] += 1
    result = max(height_state) - min(height_state)

    print('#{} {}'.format(test_case, result))

