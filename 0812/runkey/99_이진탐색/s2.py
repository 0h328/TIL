import sys
sys.stdin = open("input1.txt")

# 이진 탐색 재귀

def recursive_binary_search(numbers, target):
    if numbers == []:                       # numbers가 공백이면
        return False                        # False 반환

    start = 0                               # start를 0으로 초기화
    end = len(numbers) - 1                  # end를 numbers의 마지막 인덱스 값으로 초기화
    mid = (start + end) // 2                # mid를 start와 end의 중간 값으로 초기화

    # print(numbers, start, mid, end)

    if target == numbers[mid]:              # target이 numbers의 mid 인덱스 값이랑 같으면
        return True                         # True 반환

    elif target > numbers[mid]:             # target이 numbers의 mid 인덱스 값보다 크면
        if len(numbers) <= 2:               # numbers의 길이가 2보다 작거나 같으면
            numbers = numbers[mid:end]      # numbers를 mid부터 end까지 슬라이싱해서 담음
        else:                               # numbers의 길이가 2보다 크면
            numbers = numbers[mid:end + 1]  # numbers를 mid부터 end + 1까지 슬라이싱해서 담음
                                            # 마지막 값을 살리기 위해 + 1을 함
    elif target < numbers[mid]:             # target이 numbers의 mid 인덱스 값보다 작으면
        numbers = numbers[start:mid]        # numbers를 start부터 mid까지 슬라이싱해서 담음

    return recursive_binary_search(numbers, target)

numbers = list(map(int, input().split()))
print(recursive_binary_search(numbers, 5)) # True
print(recursive_binary_search(numbers, 10)) # False