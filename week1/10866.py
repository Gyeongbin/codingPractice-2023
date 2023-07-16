from collections import deque

inputTextLength = int(input()) #input 값 여러줄 처리해주기
inputText_list = [input() for _ in range(inputTextLength)]

deq = deque([])
isEmpty = 1
result = 0

for inputText in inputText_list :
    if(inputText=='pop_front'):
        if (isEmpty) : print(-1)
        else :
            result = deq.popleft()
            if (len(deq)==0) : isEmpty=1
            print(result)
    elif(inputText=='pop_back'):
        if (isEmpty) : print(-1)
        else :
            result = deq.pop()
            if (len(deq)==0) : isEmpty=1
            print(result)
    elif(inputText=='size'):
        print(len(deq))
    elif(inputText=='empty'):
        print(isEmpty)
    elif(inputText=='front'):
        if (isEmpty) : print(-1)
        else :
            result = deq[0]
            print(result)
    elif(inputText=='back'):
        if (isEmpty) : print(-1)
        else :
            result = deq[-1]
            print(result)
    else :
        text, X = inputText.split()
        if (text=='push_front') :
            deq.appendleft(int(X))
            if(isEmpty) : isEmpty=0
        else :
            deq.append(int(X))
            if(isEmpty) : isEmpty=0