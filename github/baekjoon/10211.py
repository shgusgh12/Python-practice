t = int(input())



def MaxSubarray(arr,low,high):
    if low == high:
        return low, high, arr[low]
    else:
        mid = (low+high) //2
        leftlow, lefthigh, leftsum = MaxSubarray(arr, low, mid)
        rightlow, righthigh, rightsum = MaxSubarray(arr, mid+1, high)
        crosslow, crosshigh, crosssum = Cross(arr, low, mid,high)

        if leftsum >= rightsum and leftsum >= crosssum:
            return leftlow, lefthigh, leftsum
        elif leftsum <= rightsum and rightsum >= crosssum:
            return rightlow, righthigh, rightsum
        else:
            return crosslow, crosshigh, crosssum


def Cross(arr, low, mid, high):
    maxleft = 0
    maxright = 0
    leftsum = -100000
    sum = 0
    for i in range(mid, low-1, -1):
        sum += arr[i]
        if sum > leftsum:
            leftsum = sum
            maxleft = i
    rightsum = -100000
    sum = 0
    for j in range(mid+1, high+1 ):
        sum += arr[j]
        if sum > rightsum:
            rightsum = sum
            maxright = j
    return maxleft, maxright, leftsum+rightsum


for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    a,b,c =MaxSubarray(arr,0,n-1)
    print(c)