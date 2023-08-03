import sys
sys.setrecursionlimit(10**6)

preorderList = []
for line in sys.stdin :
    if line == '\n': break
    else : preorderList.append(int(line.rstrip()))

def postorder(left, right):
    if left>right :
        return
    else :
        mid = right+1
        for i in range(left+1, right+1) :
            if preorderList[left] < preorderList[i] :
                mid = i
                break
        postorder(left+1, mid-1)
        postorder(mid, right)
        print(preorderList[left])

postorder(0, len(preorderList)-1)
