import sys

input = sys.stdin.readline

k = int(input())
tree = list(map(int, input().split()))
l = len(tree)
arr = [[] for _ in range(k)]

def half(low,high,i):
    #리프노드 배열에 넣고 return으로 함수 나감
    if low == high:
        arr[i].append(tree[low])
        return
    #부모노드 부터 배열에 넣는다
    root = (low + high) //2 
    arr[i].append(tree[root])
    half(low, root-1, i+1)
    half(root+1, high, i+1)

half(0,l-1,0)
for j in arr:
    # *을 붙이면 리스트 안보임
    print(*j)