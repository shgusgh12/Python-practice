import FinanceDataReader as fdr


def MaxCrossing(arr, low, mid, high):
    maxleft = 0
    maxright = 0
    leftsum = -1000000
    sum = 0
    for i in range(mid,low-1, -1):
        sum += arr[i]
        if sum > leftsum:
            leftsum = sum
            maxleft = i
    rightsum = -1000000
    sum = 0
    for j in range(mid+1, high+1):
        sum += arr[j]
        if sum > rightsum:
            rightsum = sum
            maxright = j
    return maxleft, maxright, leftsum + rightsum


def MaxSubarray(arr, low, high):
    if high == low:
        return low, high, arr[low]
    else:
        mid = (high + low)//2
        leftlow, lefthigh, leftsum = MaxSubarray(arr, low, mid)
        rightlow, righthigh, rightsum = MaxSubarray(arr, mid+1, high)
        crosslow, crosshigh, crosssum = MaxCrossing(arr,low, mid, high)

        if leftsum >= rightsum and leftsum >= crosssum:
            return leftlow, lefthigh, leftsum
        elif leftsum <= rightsum and rightsum >= crosssum:
            return rightlow, righthigh, rightsum
        else:
            return crosslow, crosshigh, crosssum

company = input('회사이름을 입력하세요: ')
start = input('시작년도 또는 날짜를 입력하세요: ')
end = input('마지막년도 또는 날짜를 입력하세요: ')

df = fdr.DataReader(company, start, end) #주말 빼고 40일

dates = df.index.tolist()

arr = []
arr.append(0)
for i in range(len(df['Close'])):
    if i+1 < len(df['Close']):
        arr.append(df['Close'][i+1]-df['Close'][i])


a,b,c = MaxSubarray(arr,0,len(arr)-1)

print('종목:',company,'매입날짜:',dates[a-1].strftime('%Y-%m-%d'),'매도날짜:',dates[b].strftime('%Y-%m-%d'),'총 수익:',c)


