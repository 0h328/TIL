import sys
sys.stdin = open('input.txt')

T = int(input())


for num1 in range(T):
    N = int(input())
    point_dict = dict()
    point_list1 = []
    point_list2 = []
    for num2 in  range(N):
        arr = list(map(int, input().split()))
        a = arr[4]
        del arr[-1]


        if a == 1:
            for i in range(arr[1], arr[-1]+1):
                for j in range(arr[0], arr[2]+1):
                    point_list1.append((j, i))
                    point_set1 = set(point_list1)
                    point_list1 = list(point_set1)

        else:
            for i in range(arr[0], arr[2]+1):
                for j in range(arr[1], arr[-1]+1):
                    point_list2.append((i, j))
                    point_set2 = set(point_list2)
                    point_list2 = list(point_set2)

    point_list1.extend(point_list2)

    for key in point_list1:
        try:
            point_dict[key] += 1
        except:
            point_dict[key] = 1
    cnt = 0

    for value in point_dict.values():
        if value >= 2:
            cnt += 1

    print("#{} {}".format(num1+1, cnt))





