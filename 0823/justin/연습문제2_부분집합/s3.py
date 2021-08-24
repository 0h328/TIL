# 참고 -> 여러가지 방식으로 코드를 작성하기
def power_set(arr, index, curr):
    if index == len(arr):
        if sum(curr) == 10:
            print(*curr)
        return

    power_set(arr, index+1, curr+[arr[index]])
    power_set(arr, index+1, curr)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
power_set(arr, 0, [])