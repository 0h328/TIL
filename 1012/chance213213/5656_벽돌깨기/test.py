

A= [[0,0],
    [0,1]]
B= [[1,2],
    [2,1]]

Ap = sum(A, [])
Bp = sum(B, [])

for i in range(len(Ap)):
    Ap[i] = Ap[i]+Bp[i]
print(Ap)