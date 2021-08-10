def counting_sort(arr: list):
    N = len(arr)
    result = [0] * N

    #1.
    # 카운팅하기 위한 배열 초기화 (누적 개수)
    counter = [0] * 10

    #2.
    # 각 요소 개수 (인덱스) 초기화
    # 각 위치의 숫자는 해당 숫자의 개수
    for i in range(N):
        counter[arr[i]] += 1
    # print(counter) # [0, 2, 1, 1, 2, 1, 0, 1, 0, 1]

    #3.
    # 이전 값을 다음 값에 누적
    # 이전 값에 다음 값을 더해가자
    for i in range(1, 10):
        counter[i] += counter[i-1]
    # print(counter) # [0, 2, 3, 4, 6, 7, 7, 8, 8, 9]

    #4.
    # 뒤부터 시작 -> 안정정렬(Stable Sorting)
    # 같은 값이 여러 개일 때 원순서상 먼저 오는 값이 앞에 오도록 하기 위함
    i = N - 1
    while i >= 0:
        # 뒤부터 시작
        result[counter[arr[i]]-1] = arr[i]
        counter[arr[i]] -= 1
        i -= 1
    # print(result) # [1, 1, 2, 3, 4, 4, 5, 7, 9]

    #5.
    # result에 있는 결과를 원본에 넣어주자
    for i in range(N):
        arr[i] = result[i]

# counting 정렬은 양의 정수여야만 함
# 주로 100만 미만까지 씀
import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print(numbers)
    counting_sort(numbers)
    print(numbers)
    ans = numbers[N-1] - numbers[0]
    print('#{} {}'.format(tc, ans))