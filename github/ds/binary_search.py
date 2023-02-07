import sys
#input = sys.stdin.readline().rstrip()

def bsearch(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        #return 다는거 잊지말기
        return bsearch(arr, target, start, mid-1)
    else:
        return bsearch(arr, target, mid+1, end)

n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

a.sort()

for x in b:
    result = bsearch(a, x, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')





