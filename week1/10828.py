class Stack:
    def __init__(self):
        self.stackArray = []
        self.isEmpty = 1
    
    def push(self, num):
        self.stackArray.append(num)
        if (self.isEmpty) : self.isEmpty=0
    
    def pop(self):
        if (self.isEmpty) : 
            return -1
        else :
            result = self.stackArray.pop(-1)
            if (len(self.stackArray)==0) : self.isEmpty=1
            return result
    
    def top(self):
        if (self.isEmpty): return -1
        else : return self.stackArray[-1]
    
    def size(self):
        return len(self.stackArray)


newStack = Stack()

inputTextLength = int(input()) #input 값 여러줄 처리해주기
inputText_list = [input() for _ in range(inputTextLength)]

for inputText in inputText_list :
    if (inputText=='pop') :
        print(newStack.pop())

    elif (inputText=='size') :
        print(newStack.size())

    elif (inputText=='empty') :
        print(newStack.isEmpty)

    elif (inputText=='top'):
        print(newStack.top())

    else :
        #push int값만 뽑아서 집어넣기
        text = inputText.split()
        newStack.push(int(text[-1]))
        # print("push",text[-1]) 
