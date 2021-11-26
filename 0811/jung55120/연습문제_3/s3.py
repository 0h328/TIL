import sys
sys.stdin = open('input.txt')

my_list = list(map(int, input().split()))

for i in range(1 << len(my_list)):
    for j in range(len(my_list)):
        if i & (1 << j):
            print(my_list[j], end=' ')
    print()
print()