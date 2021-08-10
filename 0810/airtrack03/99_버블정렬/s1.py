import sys

sys.stdin = open('input.txt')
data = list(map(int, input().split()))

def bubble_sort(num_list):
    N = len(num_list)

    for i in range(N-1, 0, -1):
        for j in range(i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

    return num_list

print(data)
print(bubble_sort(data))