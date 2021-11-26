import sys
sys.stdin = open('input.txt')

testcase = int(input())

my_list = []
for _ in range(testcase):
    room = int(input())
    box = list(map(int, input().split()))
    for _ in range(room):
        room_size = ([0] * room)
        my_list.append(room_size)
        print(my_list)

        for i in range(room):
            for j in range(box[i]):
                my_list[i][j] = 1

        max_dstance = 0
        dist = 0
        for m in range(room):
            for n in range(room):
                if my_list[m][n] == 1:

                    for o in range(m + 1, room):
                        if my_list[o][n] == 0:
                            dist += 1
                    if max_distance < dist:
                        max_distance = dist
        print(max_distance)


