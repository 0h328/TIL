import sys
sys.stdin = open('input.txt')

for _ in range(10):
    T = int(input())
    search_word = input()
    words = input()
    result = words.count(search_word)

    print('#{} {}'.format(T, result))

#1 4
#2 2
#3 19
#4 4
#5 6
#6 2
#7 5
#8 5
#9 8
#10 14