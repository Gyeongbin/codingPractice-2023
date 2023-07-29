import sys

PokeDic_int_key = {}
PokeDic_name_key = {}
testArr = []
N, M = map(int, sys.stdin.readline().split())

for i in range(N) :
    name = sys.stdin.readline().rstrip()
    PokeDic_int_key[i+1] = name
    PokeDic_name_key[name] = i+1


for _ in range(M) :
    item = sys.stdin.readline().rstrip()
    if item.isdigit() == True : #isdigit 시간 복잡도 O(n)
        print(PokeDic_int_key[int(item)])
    else :
        print(PokeDic_name_key[item])
