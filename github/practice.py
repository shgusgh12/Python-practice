

arr = [-2, -1, 1, -3, 3, 5]
n = 6

# O(n^3) 0번째 index 부터 값을 하나씩 늘려가면서 배열의 합을 구한다
# MaxSum에 최대값을 저장 
def MaxSubarray1(arr, n): 
    MaxSum = 0
    for i in range(n):
        for j in range(i,n):
            ThisSum = 0
            for k in range(i,j+1):
                ThisSum = ThisSum + arr[k]
            MaxSum = max(MaxSum, ThisSum)
    return MaxSum

def MaxSubarray2(arr, n):
    MaxSum = 0
    for i in range(n):
        ThisSum = 0
        for j in range(i,n):
            ThisSum = ThisSum + arr[j]
            MaxSum = max(MaxSum, ThisSum)
    return MaxSum

def MaxSubarray3(arr, left, right):
    
    if left == right:
        if arr[left] > 0:
            return arr[left]
        else:
            return 0

    center = (left + right) // 2
    MaxLeft = MaxSubarray3(arr, left, center)
    MaxRight = MaxSubarray3(arr, center+1, right)
    MaxCenterL = 0
    ThisSum = 0
    for i in range(center, left-1, -1):
        ThisSum = ThisSum + arr[i]
        MaxCenterL = max(MaxCenterL, ThisSum)

    MaxCenterR = 0
    ThisSum = 0

    for i in range(center+1, right+1):
        ThisSum = ThisSum + arr[i]
        MaxCenterR = max(MaxCenterR, ThisSum)
    
    MaxCenter = MaxCenterL + MaxCenterR
    MaxSum = max(max(MaxLeft, MaxRight), MaxCenter)
    return MaxSum

print(MaxSubarray3(arr,0,n-1))



def move(n, start=1, end=3, via=2):
    if n == 1:
        print(start, '에서', end, '으로 1번 원반 이동')
    else:
        move(n-1, start, via, end)
        print(start, '에서', end, '으로', n, '번 원반 이동')
        move(n-1, via, end, start)

n = int(input('원반의 개수: '))
move(n)