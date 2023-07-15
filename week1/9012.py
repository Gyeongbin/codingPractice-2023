def stackFunc(str):
    stack = []

    for i in str:
        if (i=='(') : stack.append(i)
        else :
            if(len(stack)==0) : return 0
            else : stack.pop(-1)
    
    if (len(stack)==0) : return 1
    else : return 0


num = int(input()) #input 값 여러줄 처리해주기
inputText_list = [input() for _ in range(num)]

for inputText in inputText_list :
    result = stackFunc(inputText)
    if (result) : print("YES")
    else : print("NO")