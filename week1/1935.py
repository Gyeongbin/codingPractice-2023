import sys

numArray = []
num = int(input())
text = input()

for i in range(num):
    numArray.append(int(sys.stdin.readline()))

numStack = []

for char in text :
    if (char=='+') :
        y = numStack.pop()
        x = numStack.pop()
        numStack.append(x+y)
    elif (char=='-') :
        y = numStack.pop()
        x = numStack.pop()
        numStack.append(x-y)
    elif (char=='*') :
        y = numStack.pop()
        x = numStack.pop()
        numStack.append(x*y)
    elif (char=='/') :
        y = numStack.pop()
        x = numStack.pop()
        numStack.append(x/y)
    else :
        numStack.append(numArray[ord(char)-65])

print("{:.2f}".format(numStack[0]))