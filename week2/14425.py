import sys

strArr = []
total = 0

N, M = map(int, sys.stdin.readline().split())
for _ in range(N) :
    strArr.append(sys.stdin.readline().rstrip())

for _ in range(M) :
    questStr = sys.stdin.readline().rstrip()
    if questStr in strArr :
        total += 1

print(total)