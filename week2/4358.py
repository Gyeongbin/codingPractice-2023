import sys

tree_dict = dict()
treeCount = 0

#입력방법 참고
for line in sys.stdin :
    if line == '\n':
        break
    else :
        treeName = line.rstrip()
        treeCount += 1
        if treeName in tree_dict.keys() :
            pre_val = tree_dict[treeName]
            tree_dict[treeName] = pre_val + 1
        else :
            tree_dict[treeName] = 1

for treeName in sorted(tree_dict.keys()):
    print('{} {:.4f}'.format(treeName, (tree_dict[treeName]/treeCount)*100))