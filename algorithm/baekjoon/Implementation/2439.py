N = int(input())
a = "*" * N

for i in range(N-1,-1,-1):
    print(a.replace('*',' ',i))
 