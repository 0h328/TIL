import sys
sys.stdin = open('input.txt')

def palindrome2():

    for r in range(100):
        for s in range(100):
            for i in range(50):
                if r_a[s+i] == r_a[s+50-1-i]:
                    break
            else:
                result = ''
                for k in range(s, s+50):
                    result += r_a[r][k]
                return len(result)

    for c in range(100):
        for s in range(100):
            for i in range(50):
                if c_a[s+i] == c_a[s+50-1-i]:
                    break
            else:
                result = ''
                for k in range(s, s+50):
                    result += c_a[c][k]
                return len(result)

T = 10
for tc in range(1, T + 1):
    N = int(input())
    r_a = [input() for _ in range(100)]
    # print(r_a)

    c_a = []
    for i in range(len(r_a)):
        c_a_word = ''
        for j in range(len(r_a[i])):
            c_a_word += r_a[j][i]
        c_a.append(c_a_word)
    # print(c_a)

    print(palindrome2())
