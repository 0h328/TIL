import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    pascal = [[1] * i for i in range(1, n + 1)]  # 파스칼 리스트 초기화

    # 파스칼 삼각형 리스트 생성
    for i in range(1, n):
        for j in range(1, i):
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]

    # 출력
    print(f"#{i}")
    for i in range(n):
        print(" ".join(map(str, pascal[i])))
