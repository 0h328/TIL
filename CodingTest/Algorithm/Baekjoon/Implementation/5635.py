import sys
sys.stdin = open('input.txt')

n = int(input())
person = [list(input().split()) for _ in range(n)]

person.sort(key=lambda x: (-int(x[3]), -int(x[2]), -int(x[1])))
print(person[0][0])
print(person[-1][0])




