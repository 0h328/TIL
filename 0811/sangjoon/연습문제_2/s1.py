import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    ans = 0
    r = 1
    c = 1
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # for i in range(4):
    #     # print(dr[i], dc[i])

    #     nr = r + dr[i]  # r로부터 dr만큼 이동한 새로운 nr
    #     nc = c + dc[i]  # c로부터 dc만큼 이동한 새로운 nc

    #     # 1. 벽 안으로 들어오는 경우만 수행
    #     if (0 <= nr < N) and (0 <= nc < N):
    #         print(data[nr][nc])

    #     # 2. 벽 밖으로 나가면 그냥 continue
    #     if nr < 0 or nr >= N or nc < 0 or nc >= N:
    #         continue

    print("#{} {}".format(test, ans))