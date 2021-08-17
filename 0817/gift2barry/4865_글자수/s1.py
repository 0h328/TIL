



for tc in range(int(input())):

    N = input()
    M = input()

    result = []
    for i in range(len(N)):
        result.append(M.count(N[i]))
    answer = max(result)

