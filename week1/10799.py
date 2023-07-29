#예제코드를 많이 참고함...
from collections import deque

strStack = deque(list(input()))
result = 0
pipeCount = 0
isOpen = True

while(len(strStack)>0):
    x = strStack.popleft()
    if (x=='('):
        pipeCount += 1
        isOpen = True
    elif (x==')' and isOpen) : 
        pipeCount -=1
        result += pipeCount
        isOpen = False
    else :
        pipeCount -= 1
        result += 1
        isOpen = False

print(result)
