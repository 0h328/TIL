def pascal_triangle(n: int):
    pascal = [[1 for _ in range(i)] for i in range(1, n + 1)]

    for i in range(2, n):
        for j in range(1, i):
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

    return pascal


t = int(input())

for i in range(1, t + 1):
    n = int(input())
    ans = pascal_triangle(n)

    print(f"#{i}")
    for line in ans:
        for num in line:
            print(num, end=" ")
        print("")
