import sys
sys.stdin = open('input.txt')

data = input()
check = [0] * 10

for i in range(len(data)):
    check[int(data[i])] += 1

    # 9와 6의 개수가 한쪽에 쏠리지 않고 배분하기 위한 조건
    if check[6] < check[9]:
        check[6] += 1
        check[9] -= 1
    elif check[6] > check[9]:
        check[9] += 1
        check[6] -= 1

print(max(check))

# data = input()
# check = [0] * 10
#
# nine_six = data.count('9') + data.count('6')  # 인풋에 9와 6의 개수
# for d in data:
#     if nine_six <= 1: # 1보다 작으면
#         check[int(d)] += 1    # 해당 위치에 개수를 +1
#     elif nine_six == 2:   # 개수가 2개면
#         if data.count('9') == 1 and data.count('6') == 1: # 9의 개수,6의 개수가 1개씩이면
#             check[int(d)] += 1    # 기존처럼 해당 위치에 개수를 +1
#         elif data.count('9') == 2 or data.count('6') == 2:    # 9의 개수 혹은 6의 개수가 2개씩이면
#             if d != '9' and d != '6':
#                 check[int(d)] += 1
#             elif d == '9':
#                 if check[9] == 0:
#                     check[9] += 1
#                 else:
#                     check[6] += 1
#             elif d == '6':
#                 if check[6] == 0:
#                     check[6] += 1
#                 else:
#                     check[9] += 1
#     elif nine_six >= 3:   # 9의 개수와 6의 개수가 합쳐서 3개 이상이면
#         if d != '9' and d != '6':
#             check[int(d)] += 1
#         elif d == '9':
#             if check[9] < nine_six // 2:  # 최소로 하기 위한 배분 ex) 9가 5개면 6에 3개 9에 2개 이런식으로
#                 check[9] += 1
#             else:
#                 check[6] += 1
#         elif d == '6':
#             if check[6] < nine_six // 2:
#                 check[6] += 1
#             else:
#                 check[9] += 1
#
# print(max(check))