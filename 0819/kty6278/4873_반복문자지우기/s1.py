import sys
sys.stdin = open('input.txt')

def removestring(string):
    for s in range(len(string)):
        stack.append(string[s])
        top = len(stack) - 1


for i in range(int(input())):
    string = input()
    stack = []
    removestring(string)
    print(stack)