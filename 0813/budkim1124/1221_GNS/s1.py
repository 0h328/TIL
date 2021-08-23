import sys
sys.stdin = open('input.txt')

T = int(input())

for num in range(T):
    N = str(input())
    arr = list(map(str, input().split()))
    lan_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    tmp_arr = [0] * len(arr)
    result_arr = []

    for i in range(0, len(lan_list)):
        for j in range(0, len(arr)):
            if arr[j] == lan_list[i]:
                tmp_arr[j] += lan_list.index(arr[j])


    for x in range(len(tmp_arr) - 1, 0, -1):
        for y in range(0, x):
            if tmp_arr[y] > tmp_arr[y + 1]:
                tmp_arr[y], tmp_arr[y + 1] = tmp_arr[y + 1], tmp_arr[y]


    for i in range(0, len(tmp_arr)):
        for lan in lan_list:
            if tmp_arr[i] == lan_list.index(lan):
                result_arr.append(lan)


    print("#{}\n{}".format(num+1, " ".join(result_arr)))





