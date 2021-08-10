import sys
sys.stdin = open('input.txt')

# 테스트 케이스를 받아온다.
T = int(input())
# 테스트 케이스에 맞는 양수의 개수와 양수 ai를 받아온다.
for t in range(T):
    nums = int(input())
    numbers = list(map(int, input().split()))

    # 버블 정렬을 이용하여 받아온 양수 ai 'numbers'를 정렬시켜준다.
    for i in range(nums - 1, 0, -1):
        # 'numbers'의 맨 앞에 위치한 수부터 비교
        for j in range(0, i):
            # j 번째와 j + 1 크기 비교 후, 값 변경
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    # 버블정렬로 정렬된 'numbers'의 맨 앞의 값과 맨 뒤의 가장 큰 수의 차이를 뽑아낸다.
    result = numbers[-1] - numbers[0]

    print('#{} {}'.format(t + 1, result))
