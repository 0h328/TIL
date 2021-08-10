import sys
sys.stdin = open('input.txt')

result = list(map(int, input().split(", ")))

for i in range(len(result) - 1, 0, -1):
    for j in range(0, i):
        if result[j] > result[j + 1]:
            result[j], result[j + 1] = result[j + 1], result[j]
print(result)