import sys
sys.stdin = ('input.txt')

#재귀 함수 이용

def binarySearch2(numbers, low, high, target):
    if low > high:                      # 검색 실패
        return False
    else:
        middle = (low + high) // 2
        if target == numbers[middle]:   #검색 성공
            return True
        elif target < numbers[middle]:
            return binarySearch2(numbers, low, middle-1, target)
        elif numbers[middle] < target:
            return binarySearch2(numbers, middle+1, high, target)