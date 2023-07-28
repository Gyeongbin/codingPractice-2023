import sys
from collections import deque


testCaseArr = []
all_nums = int(input())

for i in range(all_nums*2):
    data = list(map(int,sys.stdin.readline().split()))
    testCaseArr.append(data)

# testCaseArr = [[1, 0], [5], [4, 2], [1, 2, 3, 4], [6, 0], [1, 1, 9, 1, 1, 1]]

for i in range(0, all_nums*2, 2) : 
    N = testCaseArr[i][0]
    M = testCaseArr[i][1]
    nums = deque([num for num in range(N)])
    priority = deque(testCaseArr[i+1])
    count = 1

    while(1):
        if priority[0] == max(priority):
            if nums[0] == M :
                print(count)
                break
            else :
                nums.popleft()
                priority.popleft()
                count = count + 1
        else :
            goBackNum = nums.popleft()
            nums.append(goBackNum)
            goBackPriority = priority.popleft()
            priority.append(goBackPriority)