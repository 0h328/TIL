def make_set(x):
    p[x] = x


def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
        return p[x]
    else:
        return x


def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x != y:
        p[y] = x


# 1.
p = [0] * (6+1)
for i in range(7):
    make_set(i)

print(p)
print('----------------------------------')

# 2.
union(1, 3)
print(p)
print('----------------------------------')

union(2, 3)
print(p)
print('----------------------------------')

union(5, 6)
print(p)
print('----------------------------------')

# 3.
print(find_set(6))
print(find_set(3))
print(find_set(2))