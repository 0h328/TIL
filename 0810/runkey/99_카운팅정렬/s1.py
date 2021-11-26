import sys
sys.stdin = open("input.txt")

data = list(map(int, input().split(", ")))
counts = [0 for i in range(max(data) + 1)]

for i in range(len(data)):
    counts[data[i]] += 1

for j in range(len(counts) - 1):
    counts[j + 1] += counts[j]

temp = [0 for i in range(len(data))]

for k in range(len(data)-1, -1, -1):
    counts[data[k]] -= 1
    temp[counts[data[k]]] = data[k]
print(temp)