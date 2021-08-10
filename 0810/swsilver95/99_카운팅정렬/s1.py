import sys
sys.stdin = open('input.txt')

numbers = list(map(int, input().split()))


def CountingSort(numbers):
    k = max(numbers)
    count = [0] * (k + 1)                       # 최대 숫자가 k일 때 카운트 배열을 k 길이로 생성, 빈 공간 문제?
    for i in range(len(numbers)):               # counting 과정
        count[numbers[i]] += 1

    for j in range(1, k + 1):                   # counting 누적 과정
        count[j] += count[j - 1]

    tmp = [0] * len(numbers)
    for k in range(len(numbers) - 1, -1, -1):   # 같은 값이 있을 경우 앞에 놓기 위해 거꾸로
        count[numbers[k]] -= 1                  # 숫자를 한 개 넣을 공간을 만들어줌
        tmp[count[numbers[k]]] = numbers[k]     # 해당 위치에 숫자를 삽입
    return tmp

print(CountingSort(numbers))