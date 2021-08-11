import sys                                           # 행 우선 순회
sys.stdin = open('input.txt')                        # input 데이터를 불러온다.

arr = int(input( ))                                  # 'arr' 배열 크기를 받아온다.
arr_list = []                                        # 배열 크기에 맞는 데이터를 넣을 리스트를 생성

for _ in range(arr):                                 # for문을 통해 데이터를 받아온다.
    nums = list(map(int, input().split()))
    arr_list.append(nums)                            # 만들어둔 리스트에 데이터를 넣는다.
# print(arr_list)

pp_list = []
for i in range(len(arr_list)):
    for j in range(len(arr_list[i])):
        pp = arr_list[i][j]
        pp_list.append(pp)
print(pp_list)