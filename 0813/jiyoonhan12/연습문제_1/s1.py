import sys
sys.stdin = open('input.txt')


def solve(my_str1, my_str2):
    if len(my_str1) != len(my_str2): # 길이 다르면 바로 False
        return False
    else: # 길이 같으면
        for i in range(len(my_str1)): # 글자 하나하나 비교하다가
            if my_str1[i] != my_str2[i]: # 다르면 False
                return False
            # else:
            #     continue
        return True # for문 끝까지 돌렸다면 True


my_str1 = input()
my_str2 = input()

print(solve(my_str1, my_str2)) # False