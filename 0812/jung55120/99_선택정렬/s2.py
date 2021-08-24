import sys
sys.stdin = open('input.txt')

my_list = list(map(int, input().split()))
# print(my_list)

# min_idx = my_list[0]

for j in range(len(my_list)-1):
    min_idx = j
    for i in range(1+j, len(my_list)):
        if my_list[min_idx] > my_list[i]:
            min_idx = i
    my_list[j], my_list[min_idx] = my_list[min_idx], my_list[j]

print(my_list)
# print(min_idx)
