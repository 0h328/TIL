import sys
sys.stdin = open('input.txt')

for _ in range(10):
    T = int(input())
    search_word = input()
    words = input()
    result = 0
    word_length = len(words)
    for i in range(word_length):
        for j, sw in enumerate(search_word):
            if i+j == word_length or words[i+j] != sw:
                break
        else:
            result+=1

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