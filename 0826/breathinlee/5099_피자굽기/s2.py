import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())                               # N : 화덕의 크기, M : 피자 개수
    pizza = list(map(int, input().split()))          # M개의 피자에 뿌려진 치즈의 양
