import sys
sys.setrecursionlimit(10**6)


n = int(sys.stdin.readline())
tree = {}
for i in range(n):
    temp = input().split()
    tree[temp[0]] = [temp[1],temp[2]]

def inorder(i):
    if tree[i][0]!= '.':
        inorder(tree[i][0])
    print(i,end='')
    if tree[i][1]!= '.':
        inorder(tree[i][1])
def preorder(i):
    print(i,end='')
    if tree[i][0]!= '.':
        preorder(tree[i][0])
    if tree[i][1]!= '.':
        preorder(tree[i][1])   
def postorder(i):
    if tree[i][0]!= '.':
        postorder(tree[i][0])
    if tree[i][1]!= '.':
        postorder(tree[i][1])
    print(i,end='')    

preorder('A')
print()
inorder('A')
print()
postorder('A')
