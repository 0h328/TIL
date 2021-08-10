data = list(map(int, input().split()))
counts = [0] * (max(data)+1)
for i in data:
    counts[i] += 1

for i in range(1, len(counts)):
    counts[i] += counts[i-1]

res = [0] * len(data)
for i in range(len(data)):
    counts[data[i]] -= 1
    res[counts[data[i]]] = data[i]

print(res)