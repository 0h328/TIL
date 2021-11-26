import sys
sys.stdin = open('input.txt')

num = int(input())
num_list = list(map(int, input().split()))
T = int(input())
# for tc in range(T):
#     my_list = list(map(int, input().split()))
#     print(my_list)
my_list = [list(map(int, input().split())) for _ in range(T)]
print(my_list)