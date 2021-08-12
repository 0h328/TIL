import sys

sys.stdin = open('input.txt')

numbers = list(map(int, input().split()))

for i in range(1<<len(numbers)):        # 모든 부분집합의 개수만큼 반복
    tmp = []
    for j in range(len(numbers)):       # 0번째 원소 ~ n번째 원소를 탐색
        if i & (1<<j):                  # i의 j번째 비트 확인. j번째 비트가 1이 아니면 0
            tmp.append(numbers[j])      # j번째 비트가 1이면 해당 원소를 부분집합에 추가
            # print(i, j)                 # i의 j번째 비트가 1인 경우를 눈으로 보기 위해 출력
    print(' '.join(map(str, tmp)))