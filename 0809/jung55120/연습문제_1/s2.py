import sys
sys.stdin = open('input.txt')

num = int(input())
print(num)
my_list1 = list(map(int, input().split()))
print(my_list1)
T = int(input())
my_list2 = [list(map(int, input().split())) for tc in range(T)]
print(my_list2)

