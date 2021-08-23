import sys

sys.stdin = open('input.txt')

a = list(map(int, input().split()))


# 음수는???
def CountingSort(a):
    cnt = [0] * (max(a) + 1)  # 들어온 리스트에서 가장 큰 수만큼 리스트 초기화
    for i in a:  # 특정 수만큼 채워넣음
        cnt[i] += 1

    for i in range(1, len(cnt)):  # 누적합으로 초기화
        cnt[i] += cnt[i - 1]
    my_sort = [0] * len(a)  # 정렬할 리스트

    for i in range(len(a) - 1, 0, -1):
        cnt[a[i]] -= 1
        my_sort[cnt[a[i]]] = a[i]  # 정렬할 리스트의 인덱스에 하나씩 뒤에서 부터 채워넣는다


    return my_sort


print(CountingSort(a))

# for i in range(1, 4):
#     for j in range(1, 4):
#         if i != j:
#             for h in range(1, 4):
#                 if i != h and h != j:
#                     print(i, j, h)
