# dp - 또토리얼
def fact(num):
    table[0] = 1

    for i in range(1, num+1):
        table[i] = i * table[i-1]

    return table[num]

n = 10
table = [0] * (n+1)
print(fact(n))