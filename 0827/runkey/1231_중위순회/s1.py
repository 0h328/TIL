import sys
sys.stdin = open('input.txt')

def in_order(node):
    global result
    if len(V_list[node]) == 4:
        in_order(int(V_list[node][2]))
        result += V_list[node][1]
        in_order(int(V_list[node][3]))

    elif len(V_list[node]) == 3:
        in_order(int(V_list[node][2]))
        result += V_list[node][1]

    else:
        result += V_list[node][1]

    return result


for t in range(1, 11):
    result = ""
    V = int(input())
    V_list = [[0, 0, 0, 0]]
    for v in range(V):
        V_list.append(list(input().split()))
    print(V_list)
    result = in_order(1)
    print("#{} {}".format(t, result))