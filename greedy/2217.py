import sys
input = sys.stdin.readline

N = int(input().rstrip())
ropeArr = []
for i in range(N) :
    ropeArr.append(int(input().rstrip()))
ropeArr.sort()

resultArr = []
for rope in ropeArr :
    resultArr.append(rope*N)
    N -= 1

print(max(resultArr))