import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(t):
    N, M = map(int, input().split())

    result_list = []
    for _ in range(N):
        result_list.append(input())

    cnt = 0
    final = []
    for i in range(N - M):
        final = []
        for j in range(M):
            if result_list[i + j] == result_list[len(result_list) - (N - M) - i - j]:
                final.append(result_list[i + j])
                cnt = 1
            if i >= M/2:
                cnt = 1


    print("#{0} {1}".format(tc + 1, final))