import sys
sys.stdin = open('input.txt')

# 테스트 케이스를 받아온다.
T = int(input())
# 테스트 케이스에 맞는 정수의 개수 n 과 구간의 개수 m 그리고 정수 ai를 받는 'numbers'를 받아온다.
for t in range(T):
    n, m = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    # 새롭게 받아낼 이웃한 구간 합 리스트 생성
    total_list = []
    # 구간이 걸리는 부분을 제외한 부분만큼만..
    for i in range(n - m + 1):
        total = 0
        # 인접한 구간만큼의 합을 total에 입력
        for j in range(i, i + m):
            total += numbers[j]
        total_list.append(total)
    # 리스트를 오름차순으로 정렬시키고 최대 최소 차이 값 계산
    total_list.sort()
    result = total_list[-1] - total_list[0]
    print('#{} {}'.format(t+1, result))
