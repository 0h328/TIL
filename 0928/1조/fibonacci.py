def fibonacci(n):
    fib = [0, 1]

    for i in range(2, n + 1):
        fib.append(fib[i - 2] + fib[i - 1])

    return fib[n]

print(fibonacci(10000))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]