import sys
input = sys.stdin.readline

K = int(input().rstrip())
tree = [[] for _ in range(K)]
node = list(map(int, input().split()))

def traverse(list, depth, tree) :
    if (list) :
        if (len(list)==1):
            node = list.pop()
            tree[depth].append(node)
            # print(tree)
            return 0
        else :
            index = int((len(list)-1)/2)
            node = list.pop(index)
            tree[depth].append(node)
            depth += 1
            # print(tree)
            traverse(list[:index], depth, tree)
            traverse(list[index:], depth, tree)
    else :
        return 0

traverse(node, 0, tree)
for i in range(K) :
    print(' '.join(map(str, tree[i])))