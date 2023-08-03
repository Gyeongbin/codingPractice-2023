import sys
input = sys.stdin.readline

N, W = map(int, input().split())
inputList = [[] for _ in range(N+1)]
for _ in range(N-1) :
    U, V = map(int, input().split())
    inputList[U].append(V)
    inputList[V].append(U)

# 결국 리프노드에만 물이 채워진다는 것을 이용하기
leaf = 0
for i in range(N+1) :
    # 노드가 두 개뿐인 경우 1도 포함될 수 있기에 1을 제외해줄것
    if len(inputList[i]) == 1 and (i!=1):
        leaf+=1

print(W/leaf)