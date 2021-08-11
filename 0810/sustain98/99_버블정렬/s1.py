l = list(map(int, input().split()))
n = len(l)-1
for i in range(n):
    for j in range(n-i):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
print(l)
