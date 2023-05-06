import sys
from collections import defaultdict
input = sys.stdin.readline
answer = 0
n = int(input())
tree = list(map(int, input().split()))
arr = [[] for _ in range(n)]

delete = int(input())
visited = [0] * (n)

#어차피 n-1까지의 노드는 존재함 
#n-1개의 노드에서 부모노드와 제거할 노드 제거해야한다
def dfs(k):
    tree[k] = -2
    for i in range(n):
        if k == tree[i] :
            dfs(i)

dfs(delete)
#i가 -2가 아니고 tree안에 없다면 리프노드이다
for i in range(len(tree)):
    if tree[i] != -2 and i not in tree:
        answer += 1
print(answer)


#처음 생각한 경우는 자식노드가 하나일때 자식 제거하면 부모를 리프노드로
#생각하기 때문에 틀렸음 이 방식은 그 경우를 제거함