import sys
sys.stdin = open('input.txt')

def bubble_sort(result):
    for i in range(len(result) - 1, 0, -1):
        for j in range(0, i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
    return result


arr = list(map(int, input().split()))
print(bubble_sort(arr))
