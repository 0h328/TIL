def perm(n, k):
    if k == n:
        print(*p)
    else:
        for i in range(k, n):
            p[k], p[i], = p[i], p[k]
            perm(n, k+1)
            p[k], p[i], = p[i], p[k]

p = [1, 2, 3]
perm(3, 0)