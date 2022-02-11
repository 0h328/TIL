import sys
sys.stdin = open('input.txt')

# N = int(input())
#
# info = []
# for _ in range(N):
#     info.append(list(map(int, sys.stdin.readline().split())))
#
# sorted_info = sorted(info, key=lambda x: -x[2])
#
# if sorted_info[0][0] == sorted_info[1][0]:
#     print(*sorted_info[0][:2])
#     print(*sorted_info[1][:2])
#     print(*sorted_info[3][:2])
# else:
#     print(*sorted_info[0][:2])
#     print(*sorted_info[1][:2])
#     print(*sorted_info[2][:2])

N = int(input())

info = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[2], reverse=True)

ans = []
nation_cnt = []
for i in range(N):
    if len(ans) == 3:   # 길이가 3되면 끝
        break
    if nation_cnt.count(info[i][0]) < 2:    # 나라의 개수가 2개 아래일때만
        ans.append(info[i][:2])             # 국가 번호와 학생 번호 추가
        nation_cnt.append(info[i][0])       # 국가 번호 따로 추가
        continue

for i in range(3):
    print(ans[i][0], ans[i][1])
