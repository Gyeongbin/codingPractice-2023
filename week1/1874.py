import sys
from collections import deque

numArray = deque()
N = int(input())
for i in range(N):
    numArray.append(int(sys.stdin.readline()))

count = 1
stackNumArr = []
stackStrArr = []
isTrue = True

for num in numArray :
    if (num > count) :
        while(num > count) :
            stackNumArr.append(count)
            stackStrArr.append('+')
            count += 1
        stackNumArr.append(count)
        count+=1
        stackStrArr.append('+')
        stackNumArr.pop()
        stackStrArr.append('-')
    elif (num == count) :
        stackNumArr.append(count)
        count+=1
        stackStrArr.append('+')
        stackNumArr.pop()
        stackStrArr.append('-')
    else :
        if num not in stackNumArr:
            print('NO')
            isTrue = False
            break
        else :
            while(1) :
                if (num == stackNumArr[-1]) :
                    stackNumArr.pop()
                    stackStrArr.append('-')
                    break
                else : 
                    stackNumArr.pop()
                    stackStrArr.append('-')

if (isTrue) : 
    for element in stackStrArr:
        print(element)